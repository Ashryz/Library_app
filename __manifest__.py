{
    "name": "Library App",
    "author": "Tarek Ashry",
    "summary": "The Library Module by Tarek Ashry is an essential tool for managing library resources efficiently.",
    "description": """
                   This is a dynamic application designed to streamline library operations and enhance user experience.
                   Developed by Tarek Ashry,
                   this module offers a sophisticated yet intuitive platform for librarians to manage their collections effectively.
                   With features tailored to meet the diverse needs of libraries,
                   it allows for easy cataloging, indexing, and tracking of library materials.
                   """,
    "category": "Productivity",
    "application": True,
    "depends": ["base", "sale_management", "mail",],
    "data": [
        "security/ir.model.access.csv",
        "data/data.xml",
        "data/cron.xml",
        "views/base_menus.xml",
        "views/book.xml",
        "views/publisher.xml",
        "wizard/add_publisher_wizard.xml",
        "views/sale_order.xml",
        "reports/book_print.xml",
        "reports/book_print_template.xml",
    ]
}
