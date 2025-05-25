import os

# os.environ.setdefault("DATABASE_URL", "postgresql://neondb_owner:npg_mTJOzXVn1kt4@ep-bitter-mud-a2g3b5ng.eu-central-1.aws.neon.tech/click_awoke_urban_613149")

URL = "postgresql://neondb_owner:npg_mTJOzXVn1kt4@ep-bitter-mud-a2g3b5ng.eu-central-1.aws.neon.tech/fox_dock_frill_839343"
SECRET_KEY = 'django-insecure-q!_9sq!%n_oo-7_qq(0@rvhvhz!s2r$cl8!ny+sc3&zl5h_c*-'
os.environ.setdefault("DATABASE_URL", URL)
os.environ.setdefault("SECRET_KEY", SECRET_KEY)