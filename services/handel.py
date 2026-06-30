from datetime import date

def get_handlowe():

    today = date.today()

    handlowe = [
        "25.01.2026",
        "29.03.2026",
        "26.04.2026",
        "28.06.2026",
        "30.08.2026",
        "06.12.2026",
        "13.12.2026",
        "20.12.2026"
    ]

    today_format = today.strftime("%d.%m.%Y")

    if today_format in handlowe:
        status = "🟢 Сьогодні НЕДІЛЯ ТОРГОВА — магазини можуть працювати"

    else:
        status = "🔴 Сьогодні неділя неторгова — більшість магазинів закриті"

    lista = "\n".join(
        f"🛒 {x}"
        for x in handlowe
    )

    return f"""
    {status}


    📅 Торгові неділі Польща 2026:

    {lista}
    """