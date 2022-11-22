from app.models import db, User, environment, SCHEMA, Set, SetCard


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        username='Demo', email='demo@aa.io', password='password')
    leo = User(
        username='leo', email='leo@aa.io', password='password')
    turner = User(
        username='turner', email='turner@aa.io', password='password')
    mike = User(
        username='mike', email='mike@aa.io', password='password')
    vincent = User(
        username='vincent', email='vincent@aa.io', password='password')
    claude = User(
        username='claude', email='claude@aa.io', password='password')
    db.session.add(demo)
    db.session.add(leo)
    db.session.add(turner)
    db.session.add(mike)
    db.session.add(vincent)
    db.session.add(claude)
    db.session.commit()

    set_seed_data = [
        {
            "user_id": 2,
            "title": "Renaissance works of Da Vinci",
            "cards": [
                {
                    "title": "Mona Lisa",
                    "artist": "Leonardo da Vinci",
                    "display_date": "1503",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg/1200px-Mona_Lisa%2C_by_Leonardo_da_Vinci%2C_from_C2RMF_retouched.jpg",
                },
                {
                    "title": "Virgin of the Rocks",
                    "artist": "Leonardo da Vinci",
                    "display_date": "1483-1486",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e4/Leonardo_Da_Vinci_-_Vergine_delle_Rocce_%28Louvre%29.jpg/280px-Leonardo_Da_Vinci_-_Vergine_delle_Rocce_%28Louvre%29.jpg"
                },
                {
                    "title": "The Last Supper",
                    "artist": "Leonardo da Vinci",
                    "display_date": "1495-1498",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/%C3%9Altima_Cena_-_Da_Vinci_5.jpg/800px-%C3%9Altima_Cena_-_Da_Vinci_5.jpg"
                },
                {
                    "title": "Salvator Mundi",
                    "artist": "Leonardo da Vinci",
                    "display_date": "1499-1510",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5c/Leonardo_da_Vinci%2C_Salvator_Mundi%2C_c.1500%2C_oil_on_walnut%2C_45.4_%C3%97_65.6_cm.jpg/270px-Leonardo_da_Vinci%2C_Salvator_Mundi%2C_c.1500%2C_oil_on_walnut%2C_45.4_%C3%97_65.6_cm.jpg"
                },
                {
                    "title": "Lady with an Ermine",
                    "artist": "Leonardo da Vinci",
                    "display_date": "1489-1491",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f9/Lady_with_an_Ermine_-_Leonardo_da_Vinci_-_Google_Art_Project.jpg/240px-Lady_with_an_Ermine_-_Leonardo_da_Vinci_-_Google_Art_Project.jpg"
                }
            ]
        },
        {
            "user_id": 2,
            "title": "Renaissance grab bag",
            "cards": [
                {
                    "title": "The Lamentation",
                    "artist": "Giotto",
                    "display_date": "1305",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Giotto_-_Scrovegni_-_-36-_-_Lamentation_%28The_Mourning_of_Christ%29_adj.jpg/800px-Giotto_-_Scrovegni_-_-36-_-_Lamentation_%28The_Mourning_of_Christ%29_adj.jpg"
                },
                {
                    "title": "Ghent Altarpiece",
                    "artist": "Jan van Eyck",
                    "display_date": "1432",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Lamgods_open.jpg/510px-Lamgods_open.jpg"
                },
                {
                    "title": "The Baptism of Christ",
                    "artist": "Piero della Francesca",
                    "display_date": "1439-1460",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Piero_della_Francesca_-_Baptism_of_Christ_-_WGA17595.jpg/270px-Piero_della_Francesca_-_Baptism_of_Christ_-_WGA17595.jpg"
                },
                {
                    "title": "The Birth of Venus",
                    "artist": "Sandro Botticelli",
                    "display_date": "1484-1486",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg/400px-Sandro_Botticelli_-_La_nascita_di_Venere_-_Google_Art_Project_-_edited.jpg"
                },
                {
                    "title": "The School of Athens",
                    "artist": "Raphael",
                    "display_date": "1509-1511",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg/800px-%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg"
                }
            ]
        },
        {
            "user_id": 3,
            "title": "William Turner oil paintings",
            "cards": [
                {
                    "title": "The Fighting Temeraire",
                    "artist": "J. M. W. Turner",
                    "display_date": "1839",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/The_Fighting_Temeraire%2C_JMW_Turner%2C_National_Gallery.jpg/800px-The_Fighting_Temeraire%2C_JMW_Turner%2C_National_Gallery.jpg"
                },
                {
                    "title": "The Burning of the Houses of Lords and Commons",
                    "artist": "J. M. W. Turner",
                    "display_date": "1834",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Joseph_Mallord_William_Turner%2C_English_-_The_Burning_of_the_Houses_of_Lords_and_Commons%2C_October_16%2C_1834_-_Google_Art_Project.jpg/800px-Joseph_Mallord_William_Turner%2C_English_-_The_Burning_of_the_Houses_of_Lords_and_Commons%2C_October_16%2C_1834_-_Google_Art_Project.jpg"
                },
                {
                    "title": "The Slave Ship",
                    "artist": "J. M. W. Turner",
                    "display_date": "1840",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Slave-ship.jpg/800px-Slave-ship.jpg"
                },
                {
                    "title": "The Ship Wreck",
                    "artist": "J. M. W. Turner",
                    "display_date": "1805",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Joseph_Mallord_William_Turner_-_The_Shipwreck_-_Google_Art_Project.jpg/800px-Joseph_Mallord_William_Turner_-_The_Shipwreck_-_Google_Art_Project.jpg"
                },
                {
                    "title": "Dido building Carthage",
                    "artist": "J. M. W. Turner",
                    "display_date": "1815",
                    "image_url": "https://en.wikipedia.org/wiki/Dido_building_Carthage#/media/File:Turner_Dido_Building_Carthage.jpg"
                }
            ]
        },
        {
            "user_id": 3,
            "title": "Romanticism paintings grab bag",
            "cards": [
                {
                    "title": "Wanderer above the Sea of Fog",
                    "artist": "Caspar David Friedrich",
                    "display_date": "1818",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg/800px-Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg"
                },
                {
                    "title": "The Lady of Shalott",
                    "artist": "John William Waterhouse",
                    "display_date": "1888",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/John_William_Waterhouse_-_The_Lady_of_Shalott_-_Google_Art_Project_edit.jpg/800px-John_William_Waterhouse_-_The_Lady_of_Shalott_-_Google_Art_Project_edit.jpg"
                },
                {
                    "title": "The Savage State",
                    "artist": "Thomas Cole",
                    "display_date": "1834",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Cole_Thomas_The_Course_of_Empire_The_Savage_State_1836.jpg/1024px-Cole_Thomas_The_Course_of_Empire_The_Savage_State_1836.jpg"
                },
                {
                    "title": "The Third of May 1808",
                    "artist": "Francisco Goya",
                    "display_date": "1814",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/El_Tres_de_Mayo%2C_by_Francisco_de_Goya%2C_from_Prado_thin_black_margin.jpg/800px-El_Tres_de_Mayo%2C_by_Francisco_de_Goya%2C_from_Prado_thin_black_margin.jpg"
                },
                {
                    "title": "The Raft of the Medusa",
                    "artist": "Theodore Gericault",
                    "display_date": "1819",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/JEAN_LOUIS_TH%C3%89ODORE_G%C3%89RICAULT_-_La_Balsa_de_la_Medusa_%28Museo_del_Louvre%2C_1818-19%29.jpg/800px-JEAN_LOUIS_TH%C3%89ODORE_G%C3%89RICAULT_-_La_Balsa_de_la_Medusa_%28Museo_del_Louvre%2C_1818-19%29.jpg"
                }
            ]
        },
        {
            "user_id": 4,
            "title": "Michelangelo's Renaissance works",
            "cards": [
                {
                    "title": "David",
                    "artist": "Michelangelo",
                    "display_date": "1501-1504",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/%27David%27_by_Michelangelo_Fir_JBU005_denoised.jpg/800px-%27David%27_by_Michelangelo_Fir_JBU005_denoised.jpg"
                },
                {
                    "title": "Sistine Chapel ceiling",
                    "artist": "Michelangelo",
                    "display_date": "1508-1512",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/Sistine_Chapel_ceiling_02_%28brightened%29.jpg/800px-Sistine_Chapel_ceiling_02_%28brightened%29.jpg"
                },
                {
                    "title": "The Creation of Adam",
                    "artist": "Michelangelo",
                    "display_date": "1512",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg/1280px-Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg"
                },
                {
                    "title": "Pieta",
                    "artist": "Michelangelo",
                    "display_date": "1499",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Michelangelo%27s_Pieta_5450_cut_out_black.jpg/800px-Michelangelo%27s_Pieta_5450_cut_out_black.jpg"
                },
                {
                    "title": "Angel",
                    "artist": "Michelangelo",
                    "display_date": "1495",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Autori_vari%2C_arca_di_san_domenico%2C_angelo_reggicandelabro_di_michelangelo%2C_1494%2C_01.jpg/800px-Autori_vari%2C_arca_di_san_domenico%2C_angelo_reggicandelabro_di_michelangelo%2C_1494%2C_01.jpg"
                }
            ]
        },
        {
            "user_id": 4,
            "title": "Sculptures from the Renaissance",
            "cards": [
                {
                    "title": "Equestrian statue of Bartolomeo Colleoni",
                    "artist": "Andrea del Verrocchio",
                    "display_date": "1488",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Bartolomeo_Colleoni_by_Andrea_del_Verrocchio.jpg/800px-Bartolomeo_Colleoni_by_Andrea_del_Verrocchio.jpg"
                },
                {
                    "title": "David",
                    "artist": "Donatello",
                    "display_date": "1440s",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Florenz_-_Bargello_2014-08-09r.jpg/320px-Florenz_-_Bargello_2014-08-09r.jpg"
                },
                {
                    "title": "Perseus with the Head of Medusa",
                    "artist": "Benvenuto Cellini",
                    "display_date": "1545-1554",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Persee-florence.jpg/320px-Persee-florence.jpg"
                },
                {
                    "title": "The Four Seasons",
                    "artist": "Jean Goujon",
                    "display_date": "1547",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/32/Carnavalet_Jahreszeiten.jpg"
                },
                {
                    "title": "David",
                    "artist": "Michelangelo",
                    "display_date": "1501-1504",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/%27David%27_by_Michelangelo_Fir_JBU005_denoised.jpg/800px-%27David%27_by_Michelangelo_Fir_JBU005_denoised.jpg"
                }
            ]
        },
        {
            "user_id": 5,
            "title": "Paintings by Vincent Van Gogh",
            "cards": [
                {
                    "title": "The Starry Night",
                    "artist": "Vincent Van Gogh",
                    "display_date": "1889",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/800px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg"
                },
                {
                    "title": "Almond Blossoms",
                    "artist": "Vincent Van Gogh",
                    "display_date": "1890",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Vincent_van_Gogh_-_Almond_blossom_-_Google_Art_Project.jpg/800px-Vincent_van_Gogh_-_Almond_blossom_-_Google_Art_Project.jpg"
                },
                {
                    "title": "Cafe Terrace at Night",
                    "artist": "Vincent Van Gogh",
                    "display_date": "1888",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Vincent_van_Gogh_%281853-1890%29_Caf%C3%A9terras_bij_nacht_%28place_du_Forum%29_Kr%C3%B6ller-M%C3%BCller_Museum_Otterlo_23-8-2016_13-35-40.JPG/800px-Vincent_van_Gogh_%281853-1890%29_Caf%C3%A9terras_bij_nacht_%28place_du_Forum%29_Kr%C3%B6ller-M%C3%BCller_Museum_Otterlo_23-8-2016_13-35-40.JPG"
                },
                {
                    "title": "Irises",
                    "artist": "Vincent Van Gogh",
                    "display_date": "1889",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3e/Irises-Vincent_van_Gogh.jpg/300px-Irises-Vincent_van_Gogh.jpg"
                },
                {
                    "title": "Van Gogh Self Portrait",
                    "artist": "Vincent Van Gogh",
                    "display_date": "1889",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project.jpg/270px-Vincent_van_Gogh_-_Self-Portrait_-_Google_Art_Project.jpg"
                }
            ]
        },
        {
            "user_id": 5,
            "title": "Post-impressionist paintings grab bag",
            "cards": [
                {
                    "title": "A Sunday on La Grande Jatte",
                    "artist": "Georges Seurat",
                    "display_date": "1884",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Georges_Seurat_-_A_Sunday_on_La_Grande_Jatte_--_1884_-_Google_Art_Project.jpg/800px-Georges_Seurat_-_A_Sunday_on_La_Grande_Jatte_--_1884_-_Google_Art_Project.jpg"
                },
                {
                    "title": "Islands in the Rhine",
                    "artist": "Rene Schutzenberger",
                    "display_date": "1916",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/bb/Schutzenberger_Iles_du_Rhin.jpg/800px-Schutzenberger_Iles_du_Rhin.jpg"
                },
                {
                    "title": "The Large Plane Trees",
                    "artist": "Vincent van Gogh",
                    "display_date": "1889",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/03/Vincent_Willem_van_Gogh_132.jpg/761px-Vincent_Willem_van_Gogh_132.jpg"
                },
                {
                    "title": "Les cypres a Cagnes",
                    "artist": "Henri-Edmond Cross",
                    "display_date": "1908",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/3/32/Henri-Edmond_Cross%2C_1908%2C_Les_cypr%C3%A8s_%C3%A0_Cagnes%2C_oil_on_canvas%2C_81_x_100_cm%2C_Mus%C3%A9e_d%27Orsay%2C_Paris.jpg"
                },
                {
                    "title": "The Centenary of Independance",
                    "artist": "Henri Rousseau",
                    "display_date": "1892",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/Henri_Rousseau_%28French%29_-_A_Centennial_of_Independence_-_Google_Art_Project.jpg/800px-Henri_Rousseau_%28French%29_-_A_Centennial_of_Independence_-_Google_Art_Project.jpg"
                },
            ]
        },
        {
            "user_id": 6,
            "title": "Monet's Masterpiece Paintings",
            "cards": [
                {
                    "title": "La Gare Saint-Lazare",
                    "artist": "Claude Monet",
                    "display_date": "1877",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/La_Gare_Saint-Lazare_-_Claude_Monet.jpg/800px-La_Gare_Saint-Lazare_-_Claude_Monet.jpg"
                },
                {
                    "title": "Impression, Sunrise",
                    "artist": "Claude Monet",
                    "display_date": "1872",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Monet_-_Impression%2C_Sunrise.jpg/800px-Monet_-_Impression%2C_Sunrise.jpg"
                },
                {
                    "title": "The Stroll",
                    "artist": "Claude Monet",
                    "display_date": "1875",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Claude_Monet_-_Woman_with_a_Parasol_-_Madame_Monet_and_Her_Son_-_Google_Art_Project.jpg/800px-Claude_Monet_-_Woman_with_a_Parasol_-_Madame_Monet_and_Her_Son_-_Google_Art_Project.jpg"
                },
                {
                    "title": "Vetheuil in the Fog",
                    "artist": "Claude Monet",
                    "display_date": "1879",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/8/8e/Monet_-_Vetheuil_im_Nebel.jpg"
                },
                {
                    "title": "Waterlilies",
                    "artist": "Claude Monet",
                    "display_date": "Unknown Date",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Monet_-_Seerosen5.jpg/770px-Monet_-_Seerosen5.jpg"
                },
                {
                    "title": "Haystacks",
                    "artist": "Claude Monet",
                    "display_date": "1890-1891",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Claude_Monet_-_Stacks_of_Wheat_%28End_of_Summer%29_-_1985.1103_-_Art_Institute_of_Chicago.jpg/1024px-Claude_Monet_-_Stacks_of_Wheat_%28End_of_Summer%29_-_1985.1103_-_Art_Institute_of_Chicago.jpg"
                }
            ]
        },
        {
            "user_id": 6,
            "title": "Grab bag of Impressionist paintings",
            "cards": [
                {
                    "title": "Impression, Sunrise",
                    "artist": "Claude Monet",
                    "display_date": "1872",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Monet_-_Impression%2C_Sunrise.jpg/800px-Monet_-_Impression%2C_Sunrise.jpg"
                },
                {
                    "title": "View of the Canal Saint-Martin",
                    "artist": "Alfred Sisley",
                    "display_date": "1870",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/04/Alfred_Sisley_001.jpg/800px-Alfred_Sisley_001.jpg"
                },
                {
                    "title": "The Luncheon on the Grass",
                    "artist": "Edouard Manet",
                    "display_date": "1863",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/90/Edouard_Manet_-_Luncheon_on_the_Grass_-_Google_Art_Project.jpg/800px-Edouard_Manet_-_Luncheon_on_the_Grass_-_Google_Art_Project.jpg"
                },
                {
                    "title": "Haystacks",
                    "artist": "Claude Monet",
                    "display_date": "1890-1891",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/68/Claude_Monet_-_Stacks_of_Wheat_%28End_of_Summer%29_-_1985.1103_-_Art_Institute_of_Chicago.jpg/1024px-Claude_Monet_-_Stacks_of_Wheat_%28End_of_Summer%29_-_1985.1103_-_Art_Institute_of_Chicago.jpg"
                },
                {
                    "title": "Sunset at Ivry",
                    "artist": "Armand Guillaumin",
                    "display_date": "1873",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/1/13/Guillaumin_SoleilCouchantAIvry.jpg"
                },
            ]
        },
    ]

    for art_set in set_seed_data:
        new_set = Set(user_id=art_set['user_id'], title=art_set['title'])
        db.session.add(new_set)
        db.session.commit()
        for card in art_set['cards']:
            new_card = SetCard(
                set_id=new_set.id,
                title=card['title'],
                artist=card['artist'],
                image_url=card['image_url'],
                display_date=card['display_date']
            )
            db.session.add(new_card)
        db.session.commit()



# Uses a raw SQL query to TRUNCATE or DELETE the users table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_users():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.users RESTART IDENTITY CASCADE;")
    else:
        db.session.execute("DELETE FROM users")
        db.session.execute("DELETE FROM sets")
        db.session.execute("DELETE FROM set_cards")
        db.session.execute("DELETE FROM comparisons")

    db.session.commit()
