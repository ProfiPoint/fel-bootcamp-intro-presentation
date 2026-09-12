#import "@preview/touying:0.6.1": *
#import themes.university: *

#show link: underline

#let lecturer-a = sys.inputs.at("lecturer_a", default: "Alice")
#let lecturer-b = sys.inputs.at("lecturer_b", default: "Bob")
#let date = "2026-09-14"

#show: university-theme.with(
  aspect-ratio: "16-9",
  header: utils.display-current-heading(level: auto, style: auto),
  config-info(
    title: [Letní Programovací Boot Camp],
    subtitle: [Úvod],
    institution: [České vysoké učení technické v Praze, Fakulta elektrotechnická],
    author: [#lecturer-a, #lecturer-b],
    date: [#date],
  ),
  config-common(
    slide-level: 3,
  ),
)

#let spacing = 0.7em
#set par(leading: spacing, spacing: spacing)
#set list(spacing: spacing)
#set text(lang: "cs")

#title-slide()

== Kdo jsme

#align(horizon)[
  - Studenti FEL ČVUT:
    - *#lecturer-a*
    - *#lecturer-b*
  #line(length: 100%)
  - Můžete nám tykat!
]

== FEL Letní Programovací Boot Camp

#align(horizon)[
  - Pro úplné začátečníky *bez předchozí znalostí programování*
  - *Cíl:* naučit *základy programování a algoritmického myšlení*
  - *Nástroje:* *Python, Linux*
  #line(length: 100%)
  - *Lze přejít* do pokročilejší / méně pokročilé skupiny
  - LASO
]

== Ptejte se

#align(horizon)[
  - *Jsme tu pro vás!*
  - *Ptejte se!*
  #line(length: 100%)
  - *Nebojte se ptát* -- pokud Vám něco není jasné, ale bojíte se zeptat, stejný problém má pravděpodobně dalších několik lidí v učebně.
  - *Nebojte se chybovat* -- čím více uděláte chyb tady, tím méně jich uděláte během semestru.
]

== Organizační a praktické informace

#align(horizon)[
  - *Po (14. 9.) – Čt (17. 9.)*
  - *09:00* – 12:00  | 13:00 – *16:00*
  #line(length: 100%)
  - Toalety
  - Výdejna Karlovo Náměstí (menza), Kebab, Dhaba Beas, Albert, Billa...
  - Odpoledne (okolo 14:30) svačina poskytnutá fakultou
]

== Průběh Výuky

#align(horizon)[
  - Den rozdělený do 2 bloků (*Dopoledne, Odpoledne*)
  - *Teorie*, pak samostatné *programování*
  #line(length: 100%)
  - Práce na školních PC (lze i na vlastních, pokud máte Linux)
  - Dobrovolná aktivita (za bonbóny apod.)
]

== Hrubý program

#align(horizon)[
  - Po:
    - Dop.: *Linux, Proměnné*
    - Odp.: *Podmínky* (if-else)
  - Út:
    - Dop.: *For cykly*
    - Odp.: *Textové řetězce*
  - St:
    - Dop.: While cykly
    - Odp.: *Seznamy* (pole), *Knihovny*
  - Čt:
    - Dop.: *Funkce,* Dekompozice
    - Odp.: *Rekurze,* Pokročilé úlohy
]

== Programování

#align(horizon)[
  - *Proces tvorby instrukcí pro počítač*
  - Programovací jazyky
  - IDE
  - Algoritmus a algoritmické myšlení
  - Problem solving: problém $->$ řešení
]

== Velké jazykové modely (LLMs)

#align(horizon)[
  - *Nedoporučeno používat*
  - Cílem je naučit základy *Vás*
  - Bude se Vám to hodit u úloh, se kterými si LLM samo poradit neumí
]

== Prostor pro dotazy

#align(horizon)[
  - *Po (14. 9.) – Čt (17. 9.)*
  - *09:00* – 12:00  | 13:00 – *16:00*
  #line(length: 100%)
  - * Ptejte se*
  - Začátečnický programovací kurz
  - Teorie, pak programování
  - Python, Linux
  - Nepoužívat LLM (AI)
  #line(length: 100%)
  #text(fill: gray, link(
    "https://github.com/ProfiPoint/fel-programming-bootcamp-intro-presentation",
  )[github.com/ProfiPoint/fel-programming-bootcamp-intro-presentation])
]
