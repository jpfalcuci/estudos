# Git

## Introdução

Git é um sistema de controle de versões amplamente utilizado para gerenciar e rastrear alterações em projetos de software. Existem outras opções, como CVS, SVN e Mercurial, mas o Git é um dos mais populares.

### Configurações Iniciais

Inicie um repositório Git e verifique o status dos arquivos:

```bash
git init
git status
```

Configure seu nome e email local ou globalmente:

```bash
git config --local user.name "nome"
git config --global user.email "email"
```

Defina a branch padrão para repositórios novos:

```bash
git config --global init.defaultBranch main
```

### Gerenciamento de Alterações

Adicione arquivos para serem monitorados e faça commits:

```bash
git add <nome do arquivo>
git commit -m "mensagem"
```

Visualize o histórico de commits:

```bash
git log
```

Para opções de filtragem no `git log`, consulte [este link](https://devhints.io/git-log).

Crie um arquivo `.gitignore` para ignorar determinados arquivos ou pastas.

### Branches e Merging

Crie e gerencie branches para trabalhar em diferentes recursos:

```bash
git branch <nome novo branch>
git checkout <nome novo branch>
```

Crie e mude para uma nova branch em um único comando:

```bash
git checkout -b <nome novo branch>
```

Una branches usando `merge`:

```bash
git merge <nome da branch a unir>
```

Ou, use `rebase` para manter commits mais limpos:

```bash
git rebase <nome da branch a rebasear>
```

### Desfazendo Alterações

Use `git revert` para desfazer um commit:

```bash
git revert <hash do commit>
```

Salve alterações temporariamente com `git stash`:

```bash
git stash
```

### Visualizando Diferenças

Compare diferenças entre commits:

```bash
git diff <commit1>..<commit2>
```

### Tags

Crie marcos fixos no projeto usando tags:

```bash
git tag -a <nome da tag> -m "mensagem"
```

### Dicas Adicionais

- Configure o editor padrão para mensagens de commit:

  ```bash
  git config --global core.editor nano
  ```
- Corrija commits anteriores:

  - Corrija a mensagem do commit anterior:
    ```bash
    git commit -m "mensagem corrigida" --amend
    ```
  - Mude a HEAD para 3 commits atrás sem perder os arquivos:
    ```bash
    git reset --soft HEAD~3
    ```
  - Use `git rebase -i HEAD~3` para interagir com commits de forma interativa.

## GitHub e GitLab

Conectar seu repositório local ao GitHub e GitLab:

```bash
git remote add origin git@github.com:seu-nome-de-usuário/seu-repositório.git
git remote add gitlab https://gitlab.com/seu-nome-de-usuário/seu-repositório.git
```

Após realizar commits locais, faça push para ambos:

```bash
git push origin main
git push gitlab main
```

**Nota:** A flag `-u` no push limita o push à branch especificada.
