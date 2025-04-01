model = \
    {
        'Llama3.1': {
            'id': 'llama3.1:8b-instruct-q8_0',
            'access': 'local',
            'platform': 'Ollama',
            'type': 'GPT',
            'terminator': None
        },

        'DeepSeek': {
            'id': 'deepseek-r1:14b',
            'access': 'local',
            'platform': 'Ollama',
            'type': 'CoT',
            'terminator': '</think>'
        },

        'GPT 4o-mini': {
            "id": "gpt-4o-mini",
            'access': 'api',
            'platform': 'OpenAI',
            'type': 'GPT',
            'terminator': None
        },

        'o1-mini': {
            'id': 'o1-mini',
            'access': 'api',
            'platform': 'OpenAI',
            'type': 'CoT',
            'terminator': None
        },

        'o3-mini': {
            'id': 'o3-mini',
            'access': 'api',
            'platform': 'OpenAI',
            'type': 'CoT',
            'terminator': None
        },

    }

platform = \
    {
        "Ollama": {
            "model_field": "model",
            "role_field": "role",
            "content_field": "content"
            },
        "OpenAI": {
            "model_field": "model",
            "role_field": "role",
            "content_field": "content"
        }
    }