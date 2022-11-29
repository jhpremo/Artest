from app.models import db, User, environment, SCHEMA, Set, SetCard, Comparison


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
                    "notes": "depicts Italian noblewoman Lisa Gherardini, the wife of Francesco del Giocondo.",
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
                    "title": "The School of Athens",
                    "artist": "Raphael",
                    "display_date": "1509-1511",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg/800px-%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg",
                    "notes": "depicts a congregation of philosophers, mathematicians, and scientists from Ancient Greece, including Plato, Aristotle, Pythagoras, Archimedes, and Heraclitus."
                },
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
                }
            ]
        },
        {
            "user_id": 3,
            "title": "William Turner oil paintings",
            "cards": [
                {
                    "title": "The Slave Ship",
                    "artist": "J. M. W. Turner",
                    "display_date": "1840",
                    "notes": "Turner was possibly moved to paint The Slave Ship after reading about the slave ship Zong in The History and Abolition of the Slave Trade by Thomas Clarkson",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Slave-ship.jpg/800px-Slave-ship.jpg"
                },
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
                    "title": "The Ship Wreck",
                    "artist": "J. M. W. Turner",
                    "display_date": "1805",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Joseph_Mallord_William_Turner_-_The_Shipwreck_-_Google_Art_Project.jpg/800px-Joseph_Mallord_William_Turner_-_The_Shipwreck_-_Google_Art_Project.jpg"
                },
                {
                    "title": "Dido building Carthage",
                    "artist": "J. M. W. Turner",
                    "display_date": "1815",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f4/Turner_Dido_Building_Carthage.jpg/1024px-Turner_Dido_Building_Carthage.jpg"
                }
            ]
        },
        {
            "user_id": 3,
            "title": "Romanticism paintings grab bag",
            "cards": [
                {
                    "title": "The Lady of Shalott",
                    "artist": "John William Waterhouse",
                    "display_date": "1888",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/John_William_Waterhouse_-_The_Lady_of_Shalott_-_Google_Art_Project_edit.jpg/800px-John_William_Waterhouse_-_The_Lady_of_Shalott_-_Google_Art_Project_edit.jpg"
                },
                {
                    "title": "Wanderer above the Sea of Fog",
                    "artist": "Caspar David Friedrich",
                    "display_date": "1818",
                    "notes": "The painting has been widely interpreted as an emblem of self-reflection or contemplation of life's path, and the landscape is widely considered to evoke the sublime.",
                    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg/800px-Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg"
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
                    "notes": "This famous work of art depicts the body of Jesus on the lap of his mother Mary after the Crucifixion.",
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
                    "notes": "the first unsupported standing work of bronze cast during the Renaissance, and the first freestanding nude male sculpture made since antiquity.",
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
                    "notes": "This self-portrait was one of about 32 produced over a 10-year period",
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
                    "notes": "Seurat's composition includes a number of Parisians at a park on the banks of the River Seine.",
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
                    "notes": "Impression, Sunrise depicts the port of Le Havre, Monet's hometown. It is now displayed at the Musée Marmottan Monet in Paris.",
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
                    "notes": "The style of the painting breaks with the academic traditions of the time. He did not try to hide the brush strokes; the painting even looks unfinished in some parts of the scene.",
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
            notes = card.get('notes')
            new_card = SetCard(
                set_id=new_set.id,
                title=card['title'],
                artist=card['artist'],
                image_url=card['image_url'],
                display_date=card['display_date'],
                notes=notes
            )
            db.session.add(new_card)
        db.session.commit()

    comparison_seed_data = [
        {
            "user_id": 2,
            "title": "Religious renaissance fresco comparison",
            "work_1_title": "The Last Supper",
            "work_1_artist": "Leonardo da Vinci",
            "work_1_display_date": "1495-1498",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/%C3%9Altima_Cena_-_Da_Vinci_5.jpg/800px-%C3%9Altima_Cena_-_Da_Vinci_5.jpg",
            "work_2_title": "The Lamentation",
            "work_2_artist": "Giotto",
            "work_2_display_date": "1305",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Giotto_-_Scrovegni_-_-36-_-_Lamentation_%28The_Mourning_of_Christ%29_adj.jpg/800px-Giotto_-_Scrovegni_-_-36-_-_Lamentation_%28The_Mourning_of_Christ%29_adj.jpg",
            "comparison_text": """After the Betrayal of Christ (Kiss of Judas), the Lamentation of the Death of Christ is the most famous of the Scrovegni Chapel frescoes painted by Giotto in the first decade of the 14th century. The frescoes were commissioned by the wealthy Scrovegni family for their private chapel in Padua. (It is also known as the Arena Chapel because it was built on the site of an ancient Roman arena.)
The Last Supper (Italian: Il Cenacolo [il tʃeˈnaːkolo] or L'Ultima Cena [ˈlultima ˈtʃeːna]) is a mural painting by the Italian High Renaissance artist Leonardo da Vinci, dated to c. 1495–1498. The painting represents the scene of the Last Supper of Jesus with the Twelve Apostles, as it is told in the Gospel of John – specifically the moment after Jesus announces that one of his apostles will betray him.[1] Its handling of space, mastery of perspective, treatment of motion and complex display of human emotion has made it one of the Western world's most recognizable paintings and among Leonardo's most celebrated works."""
        },
        {
            "user_id": 2,
            "title": "Secular and religious renaissance frescos",
            "work_1_title": "The School of Athens",
            "work_1_artist": "Raphael",
            "work_1_display_date": "1509-1511",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/49/%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg/800px-%22The_School_of_Athens%22_by_Raffaello_Sanzio_da_Urbino.jpg",
            "work_2_title": "The Creation of Adam",
            "work_2_artist": "Michelangelo",
            "work_2_display_date": "1512",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5b/Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg/1280px-Michelangelo_-_Creation_of_Adam_%28cropped%29.jpg",
            "comparison_text": """The Creation of Adam (Italian: Creazione di Adamo) is a fresco painting by Italian artist Michelangelo, which forms part of the Sistine Chapel's ceiling, painted c. 1508–1512. It illustrates the Biblical creation narrative from the Book of Genesis in which God gives life to Adam, the first man. The fresco is part of a complex iconographic scheme and is chronologically the fourth in the series of panels depicting episodes from Genesis.
The School of Athens (Italian: Scuola di Atene) is a fresco by the Italian Renaissance artist Raphael. The fresco was painted between 1509 and 1511 as a part of Raphael's commission to decorate the rooms now known as the Stanze di Raffaello, in the Apostolic Palace in the Vatican. It depicts a congregation of philosophers, mathematicians, and scientists from Ancient Greece, including Plato, Aristotle, Pythagoras, Archimedes, and Heraclitus. The Italian artists Leonardo da Vinci and Michelangelo are also featured in the painting, shown as Plato and Heraclitus respectively."""
        },
        {
            "user_id": 3,
            "title": "Romanticism works of tragedy",
            "work_1_title": "The Third of May 1808",
            "work_1_artist": "Francisco Goya",
            "work_1_display_date": "1814",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/El_Tres_de_Mayo%2C_by_Francisco_de_Goya%2C_from_Prado_thin_black_margin.jpg/800px-El_Tres_de_Mayo%2C_by_Francisco_de_Goya%2C_from_Prado_thin_black_margin.jpg",
            "work_2_title": "The Raft of the Medusa",
            "work_2_artist": "Theodore Gericault",
            "work_2_display_date": "1819",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/15/JEAN_LOUIS_TH%C3%89ODORE_G%C3%89RICAULT_-_La_Balsa_de_la_Medusa_%28Museo_del_Louvre%2C_1818-19%29.jpg/800px-JEAN_LOUIS_TH%C3%89ODORE_G%C3%89RICAULT_-_La_Balsa_de_la_Medusa_%28Museo_del_Louvre%2C_1818-19%29.jpg",
            "comparison_text": """Completed when the artist was 27, the work has become an icon of French Romanticism. At 491 by 716 cm (16 ft 1 in by 23 ft 6 in), it is an over-life-size painting that depicts a moment from the aftermath of the wreck of the French naval frigate Méduse, which ran aground off the coast of today's Mauritania on 2 July 1816. On 5 July 1816, at least 147 people were set adrift on a hurriedly constructed raft; all but 15 died in the 13 days before their rescue, and those who survived endured starvation and dehydration and practiced cannibalism (the custom of the sea). The event became an international scandal, in part because its cause was widely attributed to the incompetence of the French captain.
In the work, Goya sought to commemorate Spanish resistance to Napoleon's armies during the occupation of 1808 in the Peninsular War. Along with its companion piece of the same size, The Second of May 1808 (or The Charge of the Mamelukes), it was commissioned by the provisional government of Spain at Goya's suggestion."""
        },
        {
            "user_id": 3,
            "title": "Turner and Fruedrich romanticism",
            "work_1_title": "Wanderer above the Sea of Fog",
            "work_1_artist": "Caspar David Friedrich",
            "work_1_display_date": "1818",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b9/Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg/800px-Caspar_David_Friedrich_-_Wanderer_above_the_sea_of_fog.jpg",
            "work_2_title": "The Slave Ship",
            "work_2_artist": "J. M. W. Turner",
            "work_2_display_date": "1840",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Slave-ship.jpg/800px-Slave-ship.jpg",
            "comparison_text": """In this classic example of a Romantic maritime painting, Turner depicts a ship visible in the background, sailing through a tumultuous sea of churning water and leaving scattered human forms floating in its wake. Turner was possibly moved to paint The Slave Ship after reading about the slave ship Zong in The History and Abolition of the Slave Trade by Thomas Clarkson the second edition of which was published in 1839.
Wanderer above the Sea of Fog is a painting by German Romantic artist Caspar David Friedrich made in 1818. It depicts a man standing upon a rocky precipice with his back to the viewer; he is gazing out on a landscape covered in a thick sea of fog through which other ridges, trees, and mountains pierce, which stretches out into the distance indefinitely. It has been considered one of the masterpieces of the Romantic movement and one of its most representative works. The painting has been widely interpreted as an emblem of self-reflection or contemplation of life's path, and the landscape is widely considered to evoke the sublime."""
        },
        {
            "user_id": 4,
            "title": "David v. David: Michelangelo and Donatello",
            "work_1_title": "David",
            "work_1_artist": "Michelangelo",
            "work_1_display_date": "1501-1504",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ec/%27David%27_by_Michelangelo_Fir_JBU005_denoised.jpg/800px-%27David%27_by_Michelangelo_Fir_JBU005_denoised.jpg",
            "work_2_title": "David",
            "work_2_artist": "Donatello",
            "work_2_display_date": "1440s",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Florenz_-_Bargello_2014-08-09r.jpg/320px-Florenz_-_Bargello_2014-08-09r.jpg",
            "comparison_text": """Donatello's bronze statue (circa 1440s) is famous as the first unsupported standing work of bronze cast during the Renaissance, and the first freestanding nude male sculpture made since antiquity. It depicts David with an enigmatic smile, posed with his foot on Goliath's severed head just after defeating the giant. The youth is completely naked, apart from a laurel-topped hat and boots, and bears the sword of Goliath.
David is a masterpiece of Renaissance sculpture, created in marble between 1501 and 1504 by the Italian artist Michelangelo. David is a 5.17-metre (17 ft 0 in) marble statue of the Biblical figure David, a favoured subject in the art of Florence. Because of the nature of the figure it represented, the statue soon came to symbolize the defence of civil liberties embodied in the Republic of Florence, an independent city-state threatened on all sides by more powerful rival states and by the hegemony of the Medici family. The eyes of David, with a warning glare, were fixated towards Rome where the Medici family lived."""
        },
        {
            "user_id": 4,
            "title": "Religious and mythological renaissance sculpture",
            "work_1_title": "Pieta",
            "work_1_artist": "Michelangelo",
            "work_1_display_date": "1499",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Michelangelo%27s_Pieta_5450_cut_out_black.jpg/800px-Michelangelo%27s_Pieta_5450_cut_out_black.jpg",
            "work_2_title": "Perseus with the Head of Medusa",
            "work_2_artist": "Benvenuto Cellini",
            "work_2_display_date": "1545-1554",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e9/Persee-florence.jpg/320px-Persee-florence.jpg",
            "comparison_text": """This famous work of art depicts the body of Jesus on the lap of his mother Mary after the Crucifixion. Michelangelo's interpretation of the Pietà is unprecedented in Italian sculpture. It is an important work as it balances the Renaissance ideals of classical beauty with naturalism.
The bronze sculpture, in which Medusa's head turns men to stone, is appropriately surrounded by three huge marble statues of men: Hercules, David, and later Neptune. Cellini's use of bronze in Perseus and the head of Medusa, and the motifs he used to respond to the previous sculpture in the piazza, were highly innovative. Examining the sculpture from the back, one can see a self-portrait of the sculptor Cellini on the back of Perseus' helmet."""
        },
        {
            "user_id": 5,
            "title": "Nightscapes by Van Gogh",
            "work_1_title": "The Starry Night",
            "work_1_artist": "Vincent Van Gogh",
            "work_1_display_date": "1889",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/800px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg",
            "work_2_title": "Cafe Terrace at Night",
            "work_2_artist": "Vincent Van Gogh",
            "work_2_display_date": "1888",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Vincent_van_Gogh_%281853-1890%29_Caf%C3%A9terras_bij_nacht_%28place_du_Forum%29_Kr%C3%B6ller-M%C3%BCller_Museum_Otterlo_23-8-2016_13-35-40.JPG/800px-Vincent_van_Gogh_%281853-1890%29_Caf%C3%A9terras_bij_nacht_%28place_du_Forum%29_Kr%C3%B6ller-M%C3%BCller_Museum_Otterlo_23-8-2016_13-35-40.JPG",
            "comparison_text": """This is the first painting in which he used starry backgrounds; he went on to paint star-filled skies in Starry Night Over the Rhône (painted the same month), and the better known The Starry Night a year later. Van Gogh also painted a starlight background in Portrait of Eugène Boch. Van Gogh mentioned the Cafe Terrace painting in a letter written to Eugène Boch on 2 October 1888, writing he had painted "a view of the café on place du Forum, where we used to go, painted at night" (emphasis van Gogh's). The constellations are depicted with such fidelity to be able to precisely date the creation of the painting to 16–17 September 1888.
Painted in June 1889, it depicts the view from the east-facing window of his asylum room at Saint-Rémy-de-Provence, just before sunrise, with the addition of an imaginary village."""
        },
        {
            "user_id": 5,
            "title": 'French pointillist paintings',
            "work_1_title": "A Sunday on La Grande Jatte",
            "work_1_artist": "Georges Seurat",
            "work_1_display_date": "1884",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/b/b7/Georges_Seurat_-_A_Sunday_on_La_Grande_Jatte_--_1884_-_Google_Art_Project.jpg/800px-Georges_Seurat_-_A_Sunday_on_La_Grande_Jatte_--_1884_-_Google_Art_Project.jpg",
            "work_2_title": "Les cypres a Cagnes",
            "work_2_artist": "Henri-Edmond Cross",
            "work_2_display_date": "1908",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/3/32/Henri-Edmond_Cross%2C_1908%2C_Les_cypr%C3%A8s_%C3%A0_Cagnes%2C_oil_on_canvas%2C_81_x_100_cm%2C_Mus%C3%A9e_d%27Orsay%2C_Paris.jpg",
            "comparison_text": """A leading example of pointillist technique, executed on a large canvas, it is a founding work of the neo-impressionist movement. Seurat's composition includes a number of Parisians at a park on the banks of the River Seine. It is in the collection of the Art Institute of Chicago.
Cross's paintings of the early- to mid-1890s are characteristically Pointillist, with closely and regularly positioned tiny dots of color. Beginning around 1895, he gradually shifted his technique, instead using broad, blocky brushstrokes and leaving small areas of exposed bare canvas between the strokes. The resulting surfaces resembled mosaics, and the paintings may be seen as precursors to Fauvism and Cubism."""
        },
        {
            "user_id": 6,
            "title": "Monet's series industrial vs. natural",
            "work_1_title": "La Gare Saint-Lazare",
            "work_1_artist": "Claude Monet",
            "work_1_display_date": "1877",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/96/La_Gare_Saint-Lazare_-_Claude_Monet.jpg/800px-La_Gare_Saint-Lazare_-_Claude_Monet.jpg",
            "work_2_title": "Waterlilies",
            "work_2_artist": "Claude Monet",
            "work_2_display_date": "Unknown Date",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Monet_-_Seerosen5.jpg/770px-Monet_-_Seerosen5.jpg",
            "comparison_text": """Gare Saint-Lazare is a series of oil paintings by the French artist Claude Monet. The paintings depict the smoky interior of this railway station in varied atmospheric conditions and from various points of view. The series contains twelve paintings, all created in 1877 in Paris. This was Monet's first series of paintings concentrating on a single theme.
Water Lilies is a series of approximately 250 oil paintings by French Impressionist Claude Monet (1840–1926). The paintings depict his flower garden at his home in Giverny, and were the main focus of his artistic production during the last thirty years of his life. Many of the works were painted while Monet suffered from cataracts."""
        },
        {
            "user_id": 6,
            "title": "Atmospheric Seascapes romanticism and impressionism",
            "work_1_title": "Impression, Sunrise",
            "work_1_artist": "Claude Monet",
            "work_1_display_date": "1872",
            "work_1_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Monet_-_Impression%2C_Sunrise.jpg/800px-Monet_-_Impression%2C_Sunrise.jpg",
            "work_2_title": "The Fighting Temeraire",
            "work_2_artist": "J. M. W. Turner",
            "work_2_display_date": "1839",
            "work_2_image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/The_Fighting_Temeraire%2C_JMW_Turner%2C_National_Gallery.jpg/800px-The_Fighting_Temeraire%2C_JMW_Turner%2C_National_Gallery.jpg",
            "comparison_text": """When Turner came to paint this picture he was at the height of his career, having exhibited at the Royal Academy, London for 40 years. He was renowned for his highly atmospheric paintings in which he explored the subjects of the weather, the sea and the effects of light. He spent much of his life near the River Thames and did many paintings of ships and waterside scenes, both in watercolour and in oils. Turner frequently made small sketches and then worked them into finished paintings in the studio.
This famous painting, Impression, Sunrise, was created from a scene in the port of Le Havre. Monet depicts a mist, which provides a hazy background to the piece set in the French harbor. The orange and yellow hues contrast brilliantly with the dark vessels, where little, if any detail is immediately visible to the audience. It is a striking and candid work that shows the smaller boats in the foreground almost being propelled along by the movement of the water. This has, once again, been achieved by separate brushstrokes that also show various colors sparkling on the sea."""
        },
    ]

    for comp in comparison_seed_data:
        new_comp = Comparison(
            user_id=comp["user_id"],
            title=comp["title"],
            work_1_title=comp["work_1_title"],
            work_1_artist=comp["work_1_artist"],
            work_1_display_date=comp["work_1_display_date"],
            work_1_image_url=comp["work_1_image_url"],
            work_2_title=comp["work_2_title"],
            work_2_artist=comp["work_2_artist"],
            work_2_display_date=comp["work_2_display_date"],
            work_2_image_url=comp["work_2_image_url"],
            comparison_text=comp["comparison_text"]
        )
        db.session.add(new_comp)
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
