import openai
from pydantic import BaseModel


openai.organization = 'org-XfVbiPgBfXfKP2hxyBIt6jvY'
openai.api_key = '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'


class Document(BaseModel):
    prompt: str = ''


def inference(prompt: str) -> list:
    print('[PROCESANDO]'.center(40, '-'))
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
          {"role": "system", "content": """Eres un calculador factorial, cada numero ingresado te calcula el factorial
          si escriben texto saldra SYNTAX ERROR"""
           },
          {"role": "user", "content": prompt}
        ]
    )
    content = completion.choices[0].message.content
    total_tokens = completion.usage.total_tokens
    print("Se han utilizado los siguientes tokens: " + total_tokens)
    print('[SE TERMINÓ DE PROCESAR]'.center(40, '-'))
    return [content, total_tokens]
