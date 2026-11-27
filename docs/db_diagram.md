Table users {
  id integer [primary key, increment]
  username varchar(50) [unique, not null]
  email varchar(255) [unique, not null]
  created_at timestamp [default: `now()`]
}

Table heroes {
  id integer [primary key, increment]
  name varchar(100) [unique, not null]
  localized_name varchar(100)
  primary_attribute varchar(20)
  attack_type varchar(20)
  roles varchar(100)
  image_url varchar(255)
}

Table drafts {
  id integer [primary key, increment]
  user_id integer [not null]
  title varchar(100)
  created_at timestamp [default: `now()`]
}

Table draft_picks {
  id integer [primary key, increment]
  draft_id integer [not null]
  hero_id integer [not null]
  team varchar(10) [not null]
  role varchar(30)
  pick_order integer [not null]
}

Ref: drafts.user_id > users.id
Ref: draft_picks.draft_id > drafts.id
Ref: draft_picks.hero_id > heroes.id