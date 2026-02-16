
# i18n/locales/ru/LC_MESSAGES/txt.ftl


# здесь лежат все пользовательские тексты
# Ключи card-* формируют содержимое карточки, а lang-* отвечает за кнопки языка.


# главный текст ответа на /start (собирается из greeting + body)
command-start_message =
   { $intro }


   { $body }


# приветствие с интерполяцией имени пользователя
card-greeting = Привет, { $username } 👋


# основное тело карточки: секции, списки, селекторы и форматирование дат/чисел
card-body =
   { -card-name } — { -card-role }
   { -card-tagline }


   { -section-about }
   { -bullet } { -card-about }
   { -bullet } { -card-experience } { NUMBER($years_exp) } { $years_exp ->
       [one] год
       [few] года
       [many] лет
      *[other] года
   }


   { -section-skills }
   { -bullet } { -card-skill-1 }
   { -bullet } { -card-skill-2 }
   { -bullet } { -card-skill-3 }


   { -section-projects } { $projects_count ->
       [one] ({ NUMBER($projects_count) } проект)
       [few] ({ NUMBER($projects_count) } проекта)
       [many] ({ NUMBER($projects_count) } проектов)
      *[other] ({ NUMBER($projects_count) } проекта)
   }
   { -bullet } { -card-project-1 }
   { -bullet } { -card-project-2 }
   { -bullet } { -card-project-3 }


   { -section-contacts }
   { -bullet } { -link-email }: { -card-email }
   { -bullet } { -link-telegram }: { -card-telegram }
   { -bullet } { -link-site }: { -card-site }
   { -bullet } { -link-github }: { -card-github }


   { -section-meta }
   { -bullet } { -meta-contact-pref }: { $contact_preference ->
       [email] { -link-email }
       [telegram] { -link-telegram }
       [site] { -link-site }
      *[other] { -meta-any-channel }
   }
   { -bullet } { -meta-availability }:
       { $availability ->
           [available] { $contact_preference ->
               [email] { -meta-available-email }
               [telegram] { -meta-available-telegram }
               [site] { -meta-available-site }
              *[other] { -meta-available-any }
           }
           [busy] { -meta-busy }
          *[other] { -meta-by-request }
       }
   { -bullet } { -meta-updated }: { DATETIME($updated_at, dateStyle: "medium") }


# кнопки выбора языка, в зависимости от параметра $checked будет выставлен чекбокс
lang-ru = { $checked ->
   [yes] ✅ Русский 🇷🇺
  *[other] Русский 🇷🇺
}
lang-en = { $checked ->
   [yes] ✅ English 🇬🇧
  *[other] English 🇬🇧
}




# заголовки секций карточки
-section-about = Описание
-section-skills = Навыки
-section-projects = Проекты
-section-contacts = Контакты / Ссылки
-section-meta = Дополнительно


# маркер списка
-bullet = •


# подписи для ссылок
-link-email = Email
-link-telegram = Telegram
-link-site = Сайт
-link-github = GitHub


# подписи и статусы для блока "Дополнительно"
-meta-contact-pref = Предпочтительный канал
-meta-availability = Доступность
-meta-updated = Обновлено
-meta-any-channel = любой канал
-meta-available-email = доступен — лучше email
-meta-available-telegram = доступен — лучше Telegram
-meta-available-site = доступен — через форму на сайте
-meta-available-any = доступен — любой канал
-meta-busy = пока не беру новые задачи
-meta-by-request = доступность по запросу


# данные карточки
-card-name = Иван Иванов
-card-role = Backend-разработчик
-card-tagline = Пишу надёжные приложения на Python.
-card-about = Разрабатывал разработку, тестировал тесты.
-card-experience = Опыт:
-card-skill-1 = Python · FastAPI · AsyncIO
-card-skill-2 = PostgreSQL · Redis · RabbitMQ
-card-skill-3 = Docker · GitHub Actions · Очень умный
-card-project-1 = MyApp — моё приложение
-card-project-2 = MyApp — моё приложение
-card-project-3 = MyApp — моё приложение
-card-email = ivan.ivanov@example.com
-card-telegram = @ivan_visit
-card-site = https://ivan-visit.dev
-card-github = github.com/ivan-visit







