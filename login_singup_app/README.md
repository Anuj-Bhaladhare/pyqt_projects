/my_pyqt_app/
│
├── main.py                            # Application entry point
├── config/                            # App configs, environment settings
│   ├── settings.py
│   └── themes.py
│
├── resources/                         # Icons, images, fonts, stylesheets
│   ├── icons/
│   ├── images/
│   └── styles.qss
│
├── ui/                                # Qt Designer .ui files
│   ├── login.ui
│   ├── main_window.ui
│   └── ...
│
├── views/                             # UI logic (views built from .ui files)
│   ├── login_view.py
│   ├── main_window_view.py
│   └── ...
│
├── controllers/                       # UI event handling / coordination logic
│   ├── login_controller.py
│   ├── main_controller.py
│   └── ...
│
├── services/                          # Business logic, application services
│   ├── auth_service.py
│   ├── file_service.py
│   └── ...
│
├── models/                            # Data models, database handling
│   ├── user_model.py
│   ├── settings_model.py
│   └── ...
│
├── database/                          # ORM, SQLite schemas, migrations
│   ├── db.py
│   ├── migrations/
│   └── ...
│
├── utils/                             # Utilities, helpers, reusable tools
│   ├── logger.py
│   ├── validators.py
│   └── ...
│
└── core/                              # Core app logic (app context, event bus)
    ├── app_context.py
    ├── event_bus.py
    └── dependency_injector.py


