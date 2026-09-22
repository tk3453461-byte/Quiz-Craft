def get_category(text):

    text = text.lower()

    categories = {

        "programming_language": [
            "programming language",
            "high-level language",
            "low-level language"
        ],

        "programming": [
            "programming",
            "object-oriented",
            "procedural",
            "functional"
        ],

        "database": [
            "database",
            "dbms",
            "sql",
            "query"
        ],

        "network": [
            "network",
            "protocol",
            "tcp",
            "http",
            "ftp",
            "ip"
        ],

        "data_structure": [
            "stack",
            "queue",
            "linked list",
            "tree",
            "graph"
        ],

        "digital": [
            "logic gate",
            "and gate",
            "or gate",
            "not gate",
            "flip-flop",
            "counter",
            "register"
        ],

        "hardware": [
            "processor",
            "memory",
            "hardware",
            "storage",
            "keyboard",
            "mouse"
        ],

        "software": [
            "software",
            "operating system",
            "compiler",
            "interpreter",
            "application"
        ]
    }

    for category, words in categories.items():

        for word in words:

            if word in text:
                return category

    return "general"
