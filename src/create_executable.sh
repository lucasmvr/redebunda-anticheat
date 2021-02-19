source ../.env/bin/activate
pyinstaller --onefile \
    --add-data="assets:assets" \
    --paths="components:screens:static:assets" \
    main.py