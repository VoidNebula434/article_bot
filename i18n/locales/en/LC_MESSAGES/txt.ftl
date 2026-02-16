
# i18n/locales/en/LC_MESSAGES/txt.ftl


command-start_message =
   { $intro }


   { $body }


card-greeting = Hello, { $username } 👋


card-body =
   { -card-name } — { -card-role }
   { -card-tagline }


   { -section-about }
   { -bullet } { -card-about }
   { -bullet } { -card-experience } { NUMBER($years_exp) } { $years_exp ->
       [one] year
      *[other] years
   }


   { -section-skills }
   { -bullet } { -card-skill-1 }
   { -bullet } { -card-skill-2 }
   { -bullet } { -card-skill-3 }


   { -section-projects } { $projects_count ->
       [one] ({ NUMBER($projects_count) } project)
      *[other] ({ NUMBER($projects_count) } projects)
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
   { -bullet } { -meta-updated }: { DATETIME($updated_at) }


lang-ru = { $checked ->
   [yes] ✅ Русский 🇷🇺
  *[other] Русский 🇷🇺
}
lang-en = { $checked ->
   [yes] ✅ English 🇬🇧
  *[other] English 🇬🇧
}


-section-about = About
-section-skills = Skills
-section-projects = Projects
-section-contacts = Contacts / Links
-section-meta = Meta


-bullet = •


-link-email = Email
-link-telegram = Telegram
-link-site = Website
-link-github = GitHub


-meta-contact-pref = Preferred contact
-meta-availability = Availability
-meta-updated = Updated
-meta-any-channel = any channel
-meta-available-email = available — prefer email
-meta-available-telegram = available — prefer Telegram
-meta-available-site = available — prefer website form
-meta-available-any = available — any channel
-meta-busy = not available for new work
-meta-by-request = availability on request


-card-name = Ivan Ivanov
-card-role = Backend Developer
-card-tagline = I build reliable Python applications.
-card-about = Built systems, tested tests.
-card-experience = Experience:
-card-skill-1 = Python · FastAPI · AsyncIO
-card-skill-2 = PostgreSQL · Redis · RabbitMQ
-card-skill-3 = Docker · GitHub Actions · Very smart
-card-project-1 = MyApp — my application
-card-project-2 = MyApp — my application
-card-project-3 = MyApp — my application
-card-email = ivan.ivanov@example.com
-card-telegram = @ivan_visit
-card-site = https://ivan-visit.dev
-card-github = github.com/ivan-visit



