
from database.connection import create_database, SessionLocal
from database.models import User, Hero, Draft, DraftPick


def seed_database():
    create_database()

    with SessionLocal() as session:
        if session.query(User).first():
            print("Тестовые данные уже существуют.")
            return

        users = [
            User(username="InvokerMain", email="invoker@example.com"),
            User(username="ShadowFiend", email="sf@example.com"),
            User(username="PudgePlayer", email="pudge@example.com"),
        ]

        heroes = [
            Hero(name="invoker", localized_name="Invoker",
                 primary_attribute="int", attack_type="Ranged",
                 roles="Carry, Nuker"),
            Hero(name="nevermore", localized_name="Shadow Fiend",
                 primary_attribute="agi", attack_type="Ranged",
                 roles="Carry, Nuker"),
            Hero(name="pudge", localized_name="Pudge",
                 primary_attribute="str", attack_type="Melee",
                 roles="Disabler, Initiator"),
            Hero(name="axe", localized_name="Axe",
                 primary_attribute="str", attack_type="Melee",
                 roles="Initiator, Durable"),
            Hero(name="juggernaut", localized_name="Juggernaut",
                 primary_attribute="agi", attack_type="Melee",
                 roles="Carry, Pusher"),
            Hero(name="crystal_maiden", localized_name="Crystal Maiden",
                 primary_attribute="int", attack_type="Ranged",
                 roles="Support, Disabler"),
            Hero(name="phantom_assassin", localized_name="Phantom Assassin",
                 primary_attribute="agi", attack_type="Melee",
                 roles="Carry, Escape"),
        ]

        session.add_all(users + heroes)
        session.flush()

        drafts = [
            Draft(user_id=users[0].id, title="Ranked Match"),
            Draft(user_id=users[1].id, title="Tournament Draft"),
        ]

        session.add_all(drafts)
        session.flush()

        picks = [
            DraftPick(draft_id=drafts[0].id, hero_id=heroes[0].id,
                      team="radiant", role="mid", pick_order=1),
            DraftPick(draft_id=drafts[0].id, hero_id=heroes[2].id,
                      team="dire", role="support", pick_order=2),
            DraftPick(draft_id=drafts[0].id, hero_id=heroes[3].id,
                      team="radiant", role="offlane", pick_order=3),
            DraftPick(draft_id=drafts[1].id, hero_id=heroes[1].id,
                      team="radiant", role="mid", pick_order=1),
        ]

        session.add_all(picks)
        session.commit()

        print("База данных успешно заполнена!")
        print(f"Пользователей: {len(users)}")
        print(f"Героев: {len(heroes)}")
        print(f"Драфтов: {len(drafts)}")
        print(f"Пиков: {len(picks)}")


if __name__ == "__main__":
    seed_database()
