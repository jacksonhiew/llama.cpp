#pragma once

// LRU cache of OpenAI Responses output items, keyed by emitted item id.
// Resolves `{type:"item_reference", id}` inputs from clients that use
// Responses `store=true` semantics.

#include <nlohmann/json.hpp>

#include <cstddef>
#include <list>
#include <mutex>
#include <string>
#include <unordered_map>

class responses_item_cache {
public:
    using json_t = nlohmann::ordered_json;

    static constexpr std::size_t CAPACITY = 4096;

    void put(const std::string & id, const json_t & item);
    bool get(const std::string & id, json_t & out);

private:
    struct entry {
        std::string id;
        json_t item;
    };

    using list_t = std::list<entry>;
    using iter_t = list_t::iterator;

    std::mutex mu;
    list_t lru; // front = MRU
    std::unordered_map<std::string, iter_t> by_id;
};
