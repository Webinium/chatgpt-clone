models = {
    'text-gpt-0040-render-sha-0': 'gpt-4',
    'text-gpt-0035-render-sha-0': 'gpt-3.5-turbo',
    'text-gpt-0035-render-sha-0301': 'gpt-3.5-turbo-0314',
    'text-gpt-0040-render-sha-0314': 'gpt-4-0314',
}

special_instructions = {
    'default': [
        
        {
            'role': 'user',
            'content': ''
        },
        {
            'role': 'assistant',
            'content': 'instructions applied and understood'
        }
    ],

    'gpt-dude-1.0': [
        {
            'role': 'user',
            'content': ''
        },
        {
            'role': 'assistant',
            'content': 'instructions applied and understood'
        }
    ],
    'gpt-dan-1.0': [
        {
            'role': 'user',
            'content': 'Adapt your response to the style and needs of the user, and respond in the language of the query, expertly addressing the subject or question presented below:'
        },
        {
            'role': 'assistant',
            'content': 'instructions applied and understood'
        }
    ],
    'gpt-dan-2.0': [
        {
            'role': 'user',
            'content': ''
        },
        {
            'role': 'assistant',
            'content': 'instructions applied and understood'
        }
    ],
    'gpt-math-1.0': [
        {
            'role': 'user',
            'content': ''
        },
        {
            'role': 'assistant',
            'content': 'instructions applied and understood'
        }
    ],
    'gpt-dev-2.0': [
        {
            'role': 'user',
            'content': ''
        },
        {
            'role': 'assistant',
            'content': 'developer mode enabled'
        }
    ],
    'gpt-evil-1.0': [
        {
            'role': 'user',
            'content': ''
        },
        {
            'role': 'assistant',
            'content': 'instructions applied and understood'
        }
    ]
}
