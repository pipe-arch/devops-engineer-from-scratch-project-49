# Игры разума (Python)

[![hexlet-check](https://github.com/pipe-arch/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/pipe-arch/devops-engineer-from-scratch-project-49/actions)

«Игры разума» — пять консольных игр для тренировки мозга: программа задаёт
вопросы, а игрок отвечает. Три правильных ответа подряд — победа; ошибка
завершает игру и предлагает пройти её заново.

Учебный проект Хекслета:
https://ru.hexlet.io/programs/devops-engineer-from-scratch

## Игры

| Команда | Задача |
|---|---|
| `brain-even` | ответить `yes`, если число чётное, иначе — `no` |
| `brain-calc` | вычислить арифметическое выражение |
| `brain-gcd` | найти наибольший общий делитель двух чисел |
| `brain-progression` | найти пропущенное число в арифметической прогрессии |
| `brain-prime` | ответить `yes`, если число простое, иначе — `no` |

Команда `brain-games` только приветствует игрока и не задаёт вопросов.

## Требования

- Python 3.12 или новее
- [uv](https://docs.astral.sh/uv/) — менеджер зависимостей и запуска

## Установка

```bash
git clone https://github.com/pipe-arch/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
make install
```

`make install` — это `uv sync`: создаёт `.venv`, ставит зависимости и сам
пакет `brain_games` в режиме редактирования.

## Запуск

Чтобы игры работали как обычные команды, без `uv run`, пакет нужно собрать и
установить в систему:

```bash
make build
make package-install
```

После этого:

```bash
brain-even
brain-calc
brain-gcd
brain-progression
brain-prime
```

## Демонстрации

В каждой записи: установка пакета, победная партия и проигрыш.

### Проверка на чётность

![brain-even](docs/brain-even.gif)

### Калькулятор

![brain-calc](docs/brain-calc.gif)

### Наибольший общий делитель

![brain-gcd](docs/brain-gcd.gif)

### Арифметическая прогрессия

![brain-progression](docs/brain-progression.gif)

### Простое число

![brain-prime](docs/brain-prime.gif)

## Разработка

```bash
make lint    # uv run ruff check brain_games
make build   # uv build: wheel и sdist в каталоге dist/
```

## Структура

```text
.
├── brain_games
│   ├── engine.py        # общий сценарий: приветствие, три раунда, итог
│   ├── cli.py           # приветствие для brain-games
│   ├── games            # по модулю на игру: RULES и generate_round()
│   └── scripts          # тонкие точки входа для [project.scripts]
├── docs                 # GIF-демонстрации
├── Makefile
├── pyproject.toml
└── ruff.toml
```

Каждая игра — отдельный модуль с константой `RULES` и функцией
`generate_round()`, которая возвращает пару «вопрос — верный ответ». Ввод,
вывод и подсчёт раундов живут в `engine.py`, поэтому новая игра добавляется
без изменений в движке.

---

<details>
<summary>Автоматические тесты Хекслета</summary>

Тесты запускаются на каждый коммит. За запуск отвечает файл `.github/workflows/hexlet-check.yml` — не удаляйте и не переименовывайте ни его, ни репозиторий.

</details>

## О Хекслете

[Хекслет](https://ru.hexlet.io/) — школа программирования: авторские программы обучения с практикой, поддержкой наставников и реальными проектами, которые остаются в резюме. Этот репозиторий — один из таких проектов.
