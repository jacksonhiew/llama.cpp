#!/usr/bin/env python
from utils import *

server: ServerProcess


def test_sidecar_force_policy_runs_one_mock_round():
    global server
    server = ServerPreset.tinyllama2()
    server.server_port = 8082
    server.n_slots = 1
    server.n_ctx = 512
    server.n_predict = 8
    server.sidecar = True
    server.sidecar_policy = "force"
    server.sidecar_mock_response = json.dumps({
        "answer": "The visible label says TEST.",
        "evidence": ["Mock sidecar evidence"],
        "ocr_text": "TEST",
        "uncertainties": [],
        "confidence": 1.0,
    })
    server.start()

    res = server.make_request("POST", "/v1/chat/completions", data={
        "stream": False,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What text is visible?"},
                    {"type": "image_url", "image_url": {"url": "https://example.invalid/image.png"}},
                ],
            },
        ],
    })

    assert res.status_code == 200
    assert res.headers.get("X-Llama-Sidecar-Rounds") == "1"
    assert res.headers.get("X-Llama-Sidecar-Policy") == "force"


def test_sidecar_max_rounds_zero_skips_orchestration():
    global server
    server = ServerPreset.tinyllama2()
    server.server_port = 8083
    server.n_slots = 1
    server.n_ctx = 512
    server.n_predict = 8
    server.sidecar = True
    server.sidecar_policy = "force"
    server.sidecar_max_rounds = 0
    server.sidecar_mock_response = json.dumps({
        "answer": "unused",
        "evidence": [],
        "ocr_text": "",
        "uncertainties": [],
        "confidence": 1.0,
    })
    server.start()

    res = server.make_request("POST", "/v1/chat/completions", data={
        "stream": False,
        "messages": [
            {"role": "user", "content": "No image here."},
        ],
    })

    assert res.status_code == 200
    assert "X-Llama-Sidecar-Rounds" not in res.headers
