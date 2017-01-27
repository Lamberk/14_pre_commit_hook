# 14_pre_commit_hook
Для правильно работы pre-commit хука, нужно создать в папке `./git/hooks/` файл `pre-commit` и перенести в него содержимое файла `pre_commit`. После этого, когда мы попытаемся сделать `git commit -m "Test commit message"` гит запустит pre-commit хук и прогонит тесты из `tests.py`. Если тесты сломаются, то он нам покажет его stdout и не сделает коммит.
