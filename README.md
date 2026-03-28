# 🔒 Sistema de Criptografia de Arquivos

Um programinha em Python que protege seus arquivos com criptografia AES — o mesmo padrão usado por bancos e grandes empresas. Simples, direto e funcional.

## O que ele faz?

Basicamente duas coisas:

- **Criptografa** uma pasta inteira de arquivos e salva tudo numa pasta nova (como um backup seguro)
- **Descriptografa** esses arquivos de volta ao original, desde que você tenha a senha certa

Sem a senha, ninguém consegue acessar o conteúdo. Simples assim.

## Como instalar

Você só precisa do Python e de uma biblioteca. Roda isso no terminal:

```
pip install pycryptodome
```

Pronto, é só isso.

## Como usar

Roda o script:

```
python criptografia.py
```

Ele vai te pedir 4 coisas:

1. **Senha** — escolha uma senha forte, ela é a chave de tudo
2. **Opção** — digite `1` para criptografar ou `2` para descriptografar
3. **Pasta origem** — a pasta com os arquivos que você quer proteger (ou restaurar)
4. **Pasta destino** — onde os arquivos processados vão ser salvos

### Exemplo prático

Digamos que você tem uma pasta chamada `meus_docs` com arquivos importantes:

**Para criptografar:**
```
Senha: minha_senha_secreta
1-Criptografar  2-Descriptografar: 1
Pasta origem: meus_docs
Pasta destino: backup_seguro
```

Os arquivos criptografados vão aparecer em `backup_seguro/` com a extensão `.enc`.

**Para descriptografar:**
```
Senha: minha_senha_secreta
1-Criptografar  2-Descriptografar: 2
Pasta origem: backup_seguro
Pasta destino: docs_restaurados
```

E pronto, seus arquivos voltam ao normal em `docs_restaurados/`.

## Como funciona por dentro

O programa segue 5 etapas:

| Etapa | O que acontece |
|-------|---------------|
| 1 | Você digita a senha e ela vira uma chave AES de 256 bits |
| 2 | O programa lê todos os arquivos da pasta de origem |
| 3 | Cada arquivo é criptografado com AES no modo CBC |
| 4 | Os arquivos protegidos são salvos na pasta de destino |
| 5 | Na hora de descriptografar, o processo inverso acontece |

## Observações

- **Não esqueça a senha!** Sem ela, não tem como recuperar os arquivos
- O programa criptografa qualquer tipo de arquivo (txt, pdf, imagens, etc.)
- Cada arquivo ganha um IV (vetor de inicialização) aleatório, o que deixa a criptografia mais segura

---

Feito com Python + PyCryptodome 🐍
