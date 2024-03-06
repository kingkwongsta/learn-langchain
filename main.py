# activate virtual env - go to .venvscripts
# enter: .\Activate.ps1

from langcorn import create_service

app = create_service(
    "cocktail:chain "
)