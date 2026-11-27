
from database.connection import create_database, SessionLocal
from database.models import User, Hero, Draft, DraftPick


def seed_database():
    create_database()

    with SessionLocal() as session:
        if session.query(User).first():
            print("Тестовые данные уже существуют.")
            return

        users = [
            User(username=f"Player{i}", email=f"player{i}@example.com")
            for i in range(1, 11)
        ]

        hero_data = [
            ("invoker", "Invoker", "int", "Ranged", "Carry, Nuker"),
            ("nevermore", "Shadow Fiend", "agi", "Ranged", "Carry, Nuker"),
            ("pudge", "Pudge", "str", "Melee", "Disabler, Initiator"),
            ("axe", "Axe", "str", "Melee", "Initiator, Durable"),
            ("juggernaut", "Juggernaut", "agi", "Melee", "Carry, Pusher"),
            ("crystal_maiden", "Crystal Maiden", "int", "Ranged", "Support, Disabler"),
            ("phantom_assassin", "Phantom Assassin", "agi", "Melee", "Carry, Escape"),
            ("lina", "Lina", "int", "Ranged", "Support, Nuker"),
            ("sven", "Sven", "str", "Melee", "Carry, Disabler"),
            ("drow_ranger", "Drow Ranger", "agi", "Ranged", "Carry, Pusher"),
        ]

        heroes = [
            Hero(
                name=name,
                localized_name=localized_name,
                primary_attribute=attribute,
                attack_type=attack_type,
                roles=roles
            )
            for name, localized_name, attribute, attack_type, roles in hero_data
        ]

        session.add_all(users + heroes)
        session.flush()

        drafts = [
            Draft(
                user_id=users[i].id,
                title=f"Draft #{i + 1}"
            )
            for i in range(10)
        ]

        session.add_all(drafts)
        session.flush()

        picks = [
            DraftPick(
                draft_id=drafts[i].id,
                hero_id=heroes[i].id,
                team="radiant" if i % 2 == 0 else "dire",
                role=["mid", "carry", "offlane", "support", "hard_support"][i % 5],
                pick_order=i + 1
            )
            for i in range(10)
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

