# Assignment 09 – Dealership Capstone (50 pts)

Django dealership app (`server/`): dealers, reviews, sentiment, auth, admin.

## Evidence files (this folder)

- `django_server`, `loginuser`, `logoutuser`, `getdealerreviews`,
  `getalldealers`, `getdealerbyid`, `getdealersbyState`, `getallcarmakes`,
  `analyzereview` – `$ curl …` + real outputs
- `CICD` – GitHub Actions run output (after push)
- `deploymentURL` – public tunnel URL (after deploy)
- Screenshots: `admin_login`, `admin_logout`, `get_dealers`,
  `get_dealers_loggedin`, `dealersbystate`, `dealer_id_reviews`,
  `dealership_review_submission`, `added_review` (+ `deployed_*` after deploy)

## GitHub URLs (repo root = this folder, name `xrwvm-fullstack_developer_capstone`)

Base: `https://github.com/Vedant-Divate/xrwvm-fullstack_developer_capstone/blob/main/…`
- Task 1: `README.md` (mentions `fullstack_developer_capstone`)
- Task 3: `server/frontend/static/About.html`
- Task 4: `server/frontend/static/Contact.html`
- Task 7: `server/frontend/src/components/Register/Register.jsx`

## Curl evidence (paste file contents)

`django_server` (`python3 manage.py runserver` + system checks), `loginuser`
(`POST /djangoapp/login`, `userName`, `status: Authenticated`), `logoutuser`
(`GET /djangoapp/logout`, empty `userName`), `getdealerreviews`
(`/fetchReviews/dealer/1` enriched), `getalldealers` (`/fetchDealers`, 50 dealers),
`getdealerbyid` (`/fetchDealer/1`), `getdealersbyState` (`/fetchDealers/Kansas`),
`getallcarmakes` (`/djangoapp/get_cars`, 15 CarModels), `analyzereview`
(`GET /analyze/Fantastic%20services`, `"sentiment": "positive"`).

## Screenshots

Local: `admin_login`, `admin_logout`, `get_dealers` (IDs+ZIPs), `get_dealers_loggedin`,
`dealersbystate`, `dealer_id_reviews`, `dealership_review_submission` (date/make/year),
`added_review` (sentiment images). Deployed (public tunnel URL in bar):
`deployed_landingpage`, `deployed_loggedin`, `deployed_dealer_detail`, `deployed_add_review`.

## CI + deploy

- `CICD`: green run with Lint Python Files + Lint JavaScript Files jobs (step IDs/durations).
- `deploymentURL`: public tunnel URL (Skills Network proxy URL unavailable here).

Test accounts: root/root123 (admin), student/student123.
Committed locally on branch `assignment-09-dealership-capstone`; `main` untouched.
