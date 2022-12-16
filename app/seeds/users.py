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
            "user_id": 1,
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
            "user_id": 1,
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
            "work_1_marker_obj":"{\"width\": 778, \"height\": 439, \"markers\": [{\"fillColor\": \"transparent\", \"strokeColor\": \"#10B981\", \"strokeWidth\": 3, \"strokeDasharray\": \"\", \"opacity\": 1, \"left\": 337, \"top\": 196, \"width\": 115, \"height\": 142, \"rotationAngle\": 0, \"visualTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"containerTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"typeName\": \"FrameMarker\", \"state\": \"select\"}, {\"color\": \"#10B981\", \"fontFamily\": \"Helvetica, Arial, sans-serif\", \"padding\": 5, \"text\": \"only figure portrayed facing forward\", \"left\": 297, \"top\": 151, \"width\": 237, \"height\": 42, \"rotationAngle\": 0, \"visualTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"containerTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"typeName\": \"TextMarker\", \"state\": \"select\"}]}",
            "work_2_marker_obj":"{\"width\": 533, \"height\": 493, \"markers\": [{\"arrowType\": \"end\", \"strokeColor\": \"#7C3AED\", \"strokeWidth\": 3, \"strokeDasharray\": \"\", \"x1\": 491, \"y1\": 164, \"x2\": 175, \"y2\": 348, \"typeName\": \"ArrowMarker\", \"state\": \"select\"}, {\"color\": \"#FFFFFF\", \"fontFamily\": \"Helvetica, Arial, sans-serif\", \"padding\": 5, \"text\": \"slope and eyes point to central  subject\", \"left\": 84, \"top\": 180, \"width\": 323, \"height\": 34, \"rotationAngle\": 0, \"visualTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"containerTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"typeName\": \"TextMarker\", \"state\": \"select\"}]}",
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
            "work_1_marker_obj": "{\"width\": 635, \"height\": 493, \"markers\": [{\"fillColor\": \"transparent\", \"strokeColor\": \"#EF4444\", \"strokeWidth\": 3, \"strokeDasharray\": \"\", \"opacity\": 1, \"left\": 290, \"top\": -5, \"width\": 70, \"height\": 507, \"rotationAngle\": 0, \"visualTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"containerTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"typeName\": \"FrameMarker\", \"state\": \"select\"}]}",
            "work_2_marker_obj":"{\"width\":778,\"height\":353,\"markers\":[{\"drawingImgUrl\":\"data:image/png;base64,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\",\"left\":2,\"top\":3,\"width\":521,\"height\":349,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FreehandMarker\",\"state\":\"select\"}]}",
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
            "work_1_marker_obj": "{\"width\": 635, \"height\": 493, \"markers\": [{\"fillColor\": \"transparent\", \"strokeColor\": \"#EF4444\", \"strokeWidth\": 3, \"strokeDasharray\": \"\", \"opacity\": 1, \"left\": 290, \"top\": -5, \"width\": 70, \"height\": 507, \"rotationAngle\": 0, \"visualTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"containerTransformMatrix\": {\"a\": 1, \"b\": 0, \"c\": 0, \"d\": 1, \"e\": 0, \"f\": 0}, \"typeName\": \"FrameMarker\", \"state\": \"select\"}]}",
            "work_2_marker_obj":"{\"width\":778,\"height\":353,\"markers\":[{\"drawingImgUrl\":\"data:image/png;base64,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\",\"left\":2,\"top\":3,\"width\":521,\"height\":349,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FreehandMarker\",\"state\":\"select\"}]}",
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
            "user_id": 1,
            "title": "Turner and Friedrich romanticism",
            "work_1_marker_obj":"{\"width\":385,\"height\":493,\"markers\":[{\"arrowType\":\"end\",\"strokeColor\":\"#2563EB\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"x1\":193,\"y1\":153,\"x2\":189,\"y2\":77,\"typeName\":\"ArrowMarker\",\"state\":\"select\"},{\"arrowType\":\"end\",\"strokeColor\":\"#2563EB\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"x1\":98,\"y1\":275,\"x2\":103,\"y2\":69,\"typeName\":\"ArrowMarker\",\"state\":\"select\"},{\"color\":\"#2563EB\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"Nature vs Man = romanticism\",\"left\":74,\"top\":27,\"width\":273,\"height\":45,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
            "work_2_marker_obj":"{\"width\":656,\"height\":493,\"markers\":[{\"drawingImgUrl\":\"data:image/png;base64,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\",\"left\":10,\"top\":274,\"width\":643,\"height\":66,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FreehandMarker\",\"state\":\"select\"},{\"color\":\"#10B981\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"Turbulent Horizon\",\"left\":437,\"top\":245,\"width\":195,\"height\":54,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
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
            "work_1_marker_obj": "{\"width\":329,\"height\":493,\"markers\":[{\"fillColor\":\"#000000\",\"strokeColor\":\"#000000\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":101,\"top\":236,\"width\":95,\"height\":56,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"EllipseMarker\",\"state\":\"select\"},{\"color\":\"#000000\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"CENSORED\",\"left\":198,\"top\":184,\"width\":125,\"height\":175,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
            "work_2_marker_obj": "{\"width\":277,\"height\":493,\"markers\":[{\"fillColor\":\"#000000\",\"strokeColor\":\"#000000\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":90,\"top\":228,\"width\":70,\"height\":62,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"EllipseMarker\",\"state\":\"select\"},{\"color\":\"#000000\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"CENSORED\",\"left\":159,\"top\":170,\"width\":106,\"height\":193,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
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
            "work_1_marker_obj":"{\"width\":493,\"height\":493,\"markers\":[{\"arrowType\":\"end\",\"strokeColor\":\"#EF4444\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"x1\":2,\"y1\":410,\"x2\":294,\"y2\":-65,\"typeName\":\"ArrowMarker\",\"state\":\"select\"},{\"arrowType\":\"end\",\"strokeColor\":\"#EF4444\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"x1\":479,\"y1\":409,\"x2\":250,\"y2\":-56,\"typeName\":\"ArrowMarker\",\"state\":\"select\"}]}",
            "work_2_marker_obj":"{\"width\":338,\"height\":493,\"markers\":[{\"bgColor\":\"#EF4444\",\"tipPosition\":{\"x\":43,\"y\":-77},\"color\":\"#FFFFFF\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"hssssssssss\",\"left\":220,\"top\":149,\"width\":100,\"height\":30,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"CalloutMarker\",\"state\":\"select\"}]}",
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
            "user_id": 1,
            "title": "Nightscapes by Van Gogh",
            "work_1_marker_obj":"{\"width\":623,\"height\":493,\"markers\":[{\"fillColor\":\"transparent\",\"strokeColor\":\"#10B981\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":143,\"top\":-14,\"width\":383,\"height\":204,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FrameMarker\",\"state\":\"select\"},{\"color\":\"#EF4444\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"\",\"left\":426,\"top\":302,\"width\":100,\"height\":30,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
            "work_2_marker_obj":"{\"width\":396,\"height\":493,\"markers\":[{\"fillColor\":\"transparent\",\"strokeColor\":\"#10B981\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":144,\"top\":-27,\"width\":178,\"height\":190,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FrameMarker\",\"state\":\"select\"}]}",
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
            "work_1_marker_obj":"{\"width\":740,\"height\":493,\"markers\":[{\"fillColor\":\"transparent\",\"strokeColor\":\"#EF4444\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":133,\"top\":23,\"width\":94,\"height\":57,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FrameMarker\",\"state\":\"select\"},{\"color\":\"#EF4444\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"very fine dot size\",\"left\":238,\"top\":27,\"width\":114,\"height\":39,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
            "work_2_marker_obj": "{\"width\":609,\"height\":493,\"markers\":[{\"fillColor\":\"transparent\",\"strokeColor\":\"#EF4444\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":450,\"top\":417,\"width\":142,\"height\":71,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FrameMarker\",\"state\":\"select\"},{\"color\":\"#EF4444\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"much larger dot size\",\"left\":437,\"top\":381,\"width\":166,\"height\":44,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
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
            "work_1_marker_obj":"{\"width\":674,\"height\":493,\"markers\":[{\"fillColor\":\"transparent\",\"strokeColor\":\"#7C3AED\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":128,\"top\":193,\"width\":186,\"height\":107,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FrameMarker\",\"state\":\"select\"},{\"color\":\"#7C3AED\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"Hint of detail in background\",\"left\":132,\"top\":153,\"width\":186,\"height\":53,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
            "work_2_marker_obj":"{\"width\":633,\"height\":493,\"markers\":[{\"fillColor\":\"transparent\",\"strokeColor\":\"#FFFF00\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":187,\"top\":41,\"width\":324,\"height\":128,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FrameMarker\",\"state\":\"select\"},{\"color\":\"#FFFF00\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"hint of detail in background\",\"left\":260,\"top\":12,\"width\":253,\"height\":28,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
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
            "work_1_marker_obj":"{\"width\":635,\"height\":493,\"markers\":[{\"fillColor\":\"#10B981\",\"strokeColor\":\"transparent\",\"strokeWidth\":0,\"strokeDasharray\":\"\",\"opacity\":0.25,\"left\":8,\"top\":170,\"width\":617,\"height\":135,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"HighlightMarker\",\"state\":\"select\"},{\"fillColor\":\"transparent\",\"strokeColor\":\"#10B981\",\"strokeWidth\":3,\"strokeDasharray\":\"\",\"opacity\":1,\"left\":9,\"top\":170,\"width\":616,\"height\":137,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FrameMarker\",\"state\":\"select\"},{\"color\":\"#10B981\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"much hazier line between nature and man\",\"left\":334,\"top\":267,\"width\":270,\"height\":111,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
            "work_2_marker_obj":"{\"width\":663,\"height\":493,\"markers\":[{\"drawingImgUrl\":\"data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAowAAAEaCAYAAACb5AYVAAAAAXNSR0IArs4c6QAAIABJREFUeF7t3c1u5Mp5BmC2kiBGAnhmnwC5lHin8SLXJGmZK8rRKr4UGwGyHglBYge2GHBmdCL1YatZZFXxq+IjZBH4kPXzfKXWO8WfPg1+uhH49U/3L6fTqcp8xnEcnr/c31TpTCcECBAgQIDArgJ10sWuUzxO558eH8aaBX0Zx1FoPM76MlMCBAgQOK5AzXxxXOVKM68dGKdpCY2ViqsbAgQIECCwo4DAuCN+7q7PA+OYuYNLi0VozAytOQIECBAgEExAYAxWkC3DeRsYp7D4dHuXtb7TPZI3MzdJluhri4NzCRAgQIAAgbwCWQNF3qFpLVWgdGCcxnMpNNplTK2W4wkQIECAQDsCAmM7tbo60hqB8VJotMt4tTwOIECAAAECzQoIjM2W7pcDrxUYp57nHrCxy9jRYjIVAgQIECDwRkBg7Gg51AyMc5em7TJ2tJhMhQABAgQICIx9roGagdEuY59ryKwIECBAgMCcgB3GjtZF7cBol7GjxWMqBAgQIEDgAwGBsaPlUTsw2mXsaPGYCgECBAgQEBiPsQbOH0Sp8RCKXcZjrC2zJECAAIFjC9hh7Kj+c9/0kvvl3XNce/XbUelMhQABAgQIhBYQGEOXJ21we73qZm6XscbuZpqOowkQIECAAIG1AgLjWrmA5+15edguY8AFYUgECBAgQCCTgMCYCTJKM3vtMu7VbxR34yBAgAABAj0LCIydVXevXca9+u2sfKZDgAABAgRCCgiMIcuybVB7XR62y7itbs4mQIAAAQJRBQTGqJXZMK653b6vt3fFa22XcUPRnEqAAAECBAILFA8Rgefe9dDmdvtqhEa7jF0vK5MjQIAAgYMKCIydFn4uuE1TLf26G7uMnS4o0yJAgACBQwsIjJ2Wfwpup+nnbH7jMAylX+a91z2UnZbStAgQIECAwO4CAuPuJSg7gD0uEZ/vMtYIqWUVtU6AAAECBI4tIDB2Xv+5S8Q1Lk3v8b3WnZfS9AgQIECAwG4CAuNu9PU63uN+Rpel69VXTwQIECBAoLSAwFhaOED7l3YZS14qFhgDFN4QCBAgQIBAJgGBMRNk9GZqX5p2H2P0FWF8BAgQIEBguYDAuNyq+SNrh8a3u4wldzObL4wJECBAgACB4AICY/AC5R7e3P2MpcKcwJi7etojQIAAAQL7CAiM+7jv1mvNXUaBcbcy65gAAQIECGQVEBizcrbRWK3QKDC2sR6MkgABAgQIXBMQGK8Jdfrfa1yaFhg7XTymRYAAAQKHExAYD1fy7xOuscsoMB50cZk2AQIECHQnIDB2V9LlE5oLjTkfgBEYl9fCkQQIECBAILKAwBi5OhXGVvIF2wJjhQLqggABAgQIVBAQGCsgR+6i5Au2BcbIlTc2AgQIECCwXEBgXG7V7ZHnu4wv4zg+f7m/2TphgXGroPMJECBAgEAMAYExRh12HUWpy9IC465l1TkBAgQIEMgmIDBmo2y3IYGx3doZOQECBAgQqCEgMNZQDt5HqfsY7TAGL7zhESBAgACBhQIC40Ko3g8rEe5KtNl7HcyPAAECBAhEFBAYI1ZlhzGVCHcl2tyBRpcECBAgQODwAgLj4ZfAd4AS4a5Em8pFgAABAgQI1BcQGOubh+yxRLgr0WZIPIMiQIAAAQKdCwiMnRd46fRKhLsSbS6dj+MIECBAgACBfAICYz7LplvKHe5KPXndNLLBEyBAgACBRgUExkYLl3vYuQNjqXc75p639ggQIECAAIHrAgLjdaNDHCEwHqLMJkmAAAECBFYJCIyr2Po7KWdgPL8cPWnl+n7q/uTNiAABAgQIxBcQGOPXqMoIcwZGl6OrlEwnBAgQIECgmoDAWI06dkcCY+z6GB0BAgQIENhTQGDcUz9Q3yUDo8vRgQptKAQIECBAYIWAwLgCrcdTSgXGcRiGp9s766zHRWNOBAgQIHAYAX/ID1PqyxPN/c7EnOFTeQgQIECAAIH9BQTG/Wuw+whyP6Qy0944juPw/OX+ZvfJGgABAgQIECCQLCAwJpP1dcLcK3C2XkY+D4yvYl9dmu5r8ZgNAQIECBxGQGA8TKl/OdG5sDgdtfUhlUuBcWp7/PZ/w2DH8cALz9QJECBAoDkBgbG5kuUb8Fyw27q7OI1uCqKn6efKUF/DowCZr6ZaIkCAAAECJQSu/U0v0ac2gwjMBcatu4tvp7Y0OL6eY/cxyMIwDAIECBAgcCYgMB50SdT++r5Pjw8vp2FYvN6m8Oiy9UEXp2kTIECAQDiBxX/Aw43cgDYJ5H4yeslgXnccX49dsvhctl4i6xgCBAgQIFBWYMnf7LIj0Hp1gRJPRq+ZxNsAuXQhCpBrpJ1DgAABAgS2CSz9O72tF2eHEih97+Kayabe7/jah/se12g7hwABAgQIpAkIjGleXRy9x+XopXBrLlu/DY/ue1wq7TgCBAgQILBcQGBcbtX8kT/C2PTkybu653wyOjfSmgBp1zF3FbRHgAABAkcXEBgPtAJKvXexJmHqfY/CY83q6IsAAQIEehUQGHut7My8egiMb6eVet+jV/UcaLGbKgECBAhkFRAYs3LGbezSk9HTyw6fv9zfxB359ZGt2XV0r+N1V0cQIECAAIFXAYHxAGshymt0alCnhEc7jjUqog8CBAgQ6EFAYOyhilfm0Nul6KUlW3rJWnBcKuo4AgQIEDiqgMDYeeXndhenKUd+Mjp3SVKC49S3y9W5K6A9AgQIEGhdQGBsvYIfjF9YfI+zNDh+C42+y7rj3wxTI0CAAIFUAYExVayh4496KfpaiVKDo13Ha6L+OwECBAj0LiAwdlphu4vXC5vygMzrruNrqy5bX/d1BAECBAj0IyAw9lPLdzOJ+H3RkalTdh1f53Gk+0Aj187YCBAgQKC8gMBY3rh6D0d6jU5u3JRdx3EYhqfbO79DuYugPQIECBAIJ+CPXbiSbB+Q3cXthlML177HWmDM46wVAgQIEIgvIDDGr1HSCO0uJnElHTxn67J0EqGDCRAgQKBRAYGx0cLNDduDLuWLeb57a5exvLkeCBAgQGB/AYFx/xpkG4HX6GSjvNiQwFjeWA8ECBAgEE9AYIxXk9Ujcu/iarrFJ57v4tphXEznQAIECBBoWEBgbLh4b4fu/rp6hTwP5u5jrGevJwIECBDYR0Bg3Mc9e68ulWYndVm6HqmeCBAgQCC4gMAYvEBLhycwLpXafhzr7YZaIECAAIG2BATGtuo1O1qXo+sW0X2Mdb31RoAAAQL7CwiM+9dg8wjseG0mTG7grbkHX5L5nECAAAECjQkIjI0VbG64AmP9Inrwpb65HgkQIEBgPwGBcT/7bD0LL9koFzfkFUaLqRxIgAABAh0ICIwdFNHl0fpF9JL0+uZ6JECAAIH9BATG/eyz9OwBjCyMyY34zu5kMicQIECAQMMCAmPDxZuG7v7F/QoorO9nr2cCBAgQqCsgMNb1zt6bwJidNKlB948mcTmYAAECBBoVEBgbLdw0bO9f3L94Avv+NTACAgQIECgvIDCWNy7Wg7BSjHZxw2qwmMqBBAgQINCwgMDYcPGElf2L5z7G/WtgBAQIECBQXkBgLG9crAf3zxWjTWrYa42SuBxMgAABAg0KCIwNFm0asp2tOIUTGOPUwkgIECBAoIyAwFjGtXirLkcXJ17cgcC4mMqBBAgQINCogMDYaOEExjiFExjj1MJICBAgQKCMgMBYxrV4q58fH8a3nbyM4/j85f6meMc6+IWAwGhRECBAgEDvAgJjgxX+9PjwchqGn2s3DsP4dHsnLO5US4FxJ3jdEiBAgEA1AYGxGnW+js4vR3+9vVPHfLzJLQmMyWROIECAAIHGBASNxgrm6eh4BRMY49XEiAgQIEAgr4DAmNezeGsedilOnNyBwJhM5gQCBAgQaExAYGyoYHPfHT09+fLkkvSuVRQYd+XXOQECBAhUEBAYKyDn6uJ8d3Fq19PRuXTXtyMwrrdzJgECBAi0ISAwtlGnb6N0OTpmsQTGmHUxKgIECBDIJyAw5rMs3pLvji5OvKoDgXEVm5MIECBAoCEBgbGRYnk6Om6hBMa4tTEyAgQIEMgjIDDmcSzeisvRxYlXdyAwrqZzIgECBAg0IiAwNlIogTFuoQTGuLUxMgIECBDIIyAw5nEs3or7F4sTr+5AYFxN50QCBAgQaERAYGykUEJJ3EKpTdzaGBkBAgQI5BEQGPM4Fm9FKClOvLoDtVlN50QCBAgQaERAYGykUEJJ3EKpTdzaGBkBAgQI5BEQGPM4Fm9FKClOvLoDtVlN50QCBAgQaERAYGykUEJJ3EKpTdzaGBkBAgQI5BEQGPM4Fm9FKClOvLoDtVlN50QCBAgQaERAYGykUEJJ3EJ55VHc2hgZAQIECOQREBjzOBZvRWAsTry6Ay9VX03nRAIECBBoREBgbKRQAmPcQgmMcWtjZAQIECCQR0BgzONYvBWBsTjx6g5+/dP9y83p9PPv0jgMw9Ptnd+t1aJOJECAAIFoAv6oRavIhfEIjLELpT6x62N0BAgQILBNQGDc5lftbIGkGvWqjtRnFZuTCBAgQKARAYGxkUIJJLELpT6x62N0BAgQILBNQGDc5lftbIGkGvWqjrxaZxWbkwgQIECgEQGBsZFCCYyxC+VJ6dj1MToCBAgQ2CYgMG7zq3a2wFiNelVHAuMqNicRIECAQCMCAmMjhRIYYxfq/NU602hfxnF8/nJ/E3vkRkeAAAECBK4LCIzXjUIcITCGKMOHg7DLGL9GRkiAAAEC6wQExnVu1c8SGKuTJ3coMCaTOYEAAQIEGhEQGBsplKdw4xfKZen4NTJCAgQIEFgnIDCuc6t+1nlgnAbgHrnqZbjaoV3Gq0QOIECAAIEGBQTGRoo2Fxh9Z3G84gn28WpiRAQIECCwXUBg3G5YpYW5y50CYxX6pE7UKYnLwQQIECDQiIDA2EihpmG6R66NYtllbKNORkmAAAECywUExuVWIY50j1yIMnw4iLlgP53gntP4tTNCAgQIEJgXEBgbWxkCYxsFc89pG3UySgIECBBYJiAwLnMKc5TL0mFKYZexjVIYJQECBAhkEBAYMyDWbsIuY23xdf15AGadm7MIECBAIJ6AwBivJldHJDBeJQpzgAdgwpTCQAgQIEBgg4DAuAFvr1PPd668XmevSlzv1y7jdSNHECBAgEB8AYExfo1mR+i7pdspnF3GdmplpAQIECAwLyAwNroyBMZ2Cuc1O+3UykgJECBAQGDsag0IjG2V02t22qqX0RIgQIDAewE7jI2uCIGxrcLZZWyrXkZLgAABAgJjF2tAYGyvjB6Aaa9mRkyAAAEC3wXsMDa6EgTGNgvnAZg262bUBAgQOLqAwNjoChAY2yycS9Nt1s2oCRAgcHQBgbHRFSAwNlq4YRjmdhmn2byM4/j85f6m3ZkZOQECBAj0KiAwNlpZgbHRwg3DcGmXUWhst6ZGToAAgd4FBMZGKywwNlq4H8MWGtuun9ETIEDgaAICY6MVFxgbLdybYX8UGsdhGMdxHFyibr/OZkCAAIEeBATGRqsoMDZauLNhfxQap0MFxz7qbBYECBBoXUBgbLSCAmOjhZsZ9oLQODzd3vld7afkZkKAAIHmBPwRaq5k3wcsMDZauAvDnkLjafq58N+nncan2ztPUPdVdrMhQIBAMwICYzOlej9QgbHRwl0Z9pLg6N7GPmtvVgQIEIgsIDBGrs4HYxMYGy3cwmFfelfj6+lfXaJeKOkwAgQIEMghIDDmUNyhDYFxB/SKXb7uNE5dfnSZ2m5jxaLoigABAgcWEBgbLP75QxLjMHgoosE6pgz58+PDVObZH98QkyLpWAIECBBYIyAwrlHb+Zzzy5UC484FqdD9knsbp2HYcaxQDF0QIEDggAICY4NFFxgbLFrGIX+02zh1Y8cxI7amCBAgQOCbgMDY2EKYe2efgNBYETcO99p7G4XGjcBOJ0CAAIFfCAiMjS0Ku4uNFazQcD0UUwhWswQIECAwKyAwNrQw5naW3L/YUAELDfXajqMd6ELwmiVAgMCBBATGhoo9924+YaChAhYcqtBYEFfTBAgQIOAexpbWgMvRLVWr/lg/epLaTnT9euiRAAECPQnYYWykmh52aaRQAYZ5abfRbnSA4hgCAQIEGhUQGBspnN3FRgoVZJiXQuP47VWN4/D85f4myFANgwABAgQaEBAYGyjSNESBsZFCBRrmpe+jdnk6UJEMhQABAo0ICIyNFOr8j7/Li40UbsdhfvQgjPWzY2F0TYAAgQYFBMYGiua7oxsoUtAhXnoQxi5j0IIZFgECBIIKCIxBC/N2WC5HN1Ck4EOcuzztfsbgRTM8AgQIBBIQGAMV49JQBMYGihR8iC5PBy+Q4REgQCC4gMAYvEDT8Ny/2ECRGhjipYdgpqG7p7GBAhoiAQIEdhQQGHfEX9K1+xeXKDlmiYAXey9RcgwBAgQIzAkIjIHXhe+ODlychofmHY0NF8/QCRAgsJOAwLgT/JJuLzyoMDzd3qnbEkDHXBRwT6PFQYAAAQIpAoJHilblY+cCo3vNKheh4+7c09hxcU2NAAECmQUExsyguZrz3dG5JLVzSeCjexqnc7x2x9ohQIAAgVcBgTHoWvAqnaCF6XBYH12enqZrV7vDopsSAQIEEgUExkSwGod72KWGsj7eCnwUGn0rjLVCgAABAgJjwDXg3sWARTnAkD66RG2X8QALwBQJECDwgYDAGHB5uBwdsCgHGtKl3Uah8UCLwFQJECBwJiAwBlsSHnYJVpCDDscrnQ5aeNMmQIDABQGBMdDScO9ioGIcfCh2GQ++AEyfAAECdhjjrgG7OnFrc8SR+QfMEatuzgQIEJgXsMMYZGXY0QlSCMN4J+ABLAuCAAECBCYBgTHIOvCHOUghDOOdgF1GC4IAAQIEBMYga8Af5SCFMIxZAU/tWxgECBAgYIcxwBqwuxigCIZwUeD8HzRe5G2xECBA4HgCAuPONbe7uHMBdL9I4O0/agTGRWQOIkCAQFcCAuOO5fSgy474uk4SEBiTuBxMgACB7gQExp1Keiks2r3ZqSC6/VBAYLRACBAgcGwBgXGn+s/dtzgNxdev7VQQ3QqM1gABAgQIXBQQGHdYHC5F74Cuy00Cdhg38TmZAAECzQsIjJVLKCxWBtddFgGBMQujRggQINCsgMBYsXTuW6yIrausAgJjVk6NESBAoDkBgbFSyS6Fxal79y1WKoJuVgsIjKvpnEiAAIEuBATGCmUUFisg66KogMBYlFfjBAgQCC8gMBYukbBYGFjzVQTOn+q3K16FXScECBAIIyAwFiyFsFgQV9NVBXyfdFVunREgQCCcgMBYqCTCYiFYze4iIDDuwq5TAgQIhBEQGAuVwou5C8FqdheB838A+UaiXcqgUwIECOwmIDAWoPeuxQKomtxdwIMvu5fAAAgQILCbgMCYmV5YzAyquTACAmOYUhgIAQIEqgsIjJnJ5y5Fu3yXGVlzuwgIjLuw65QAAQIhBATGjGWwu5gRU1PhBATGcCUxIAIECFQTEBgzUs/tLnpfXUZgTe0qIDDuyq9zAgQI7CogMGbin9tddCk6E65mQgh4eXeIMhgEAQIEdhEQGDOx213MBKmZsALexRi2NAZGgACB4gICYwZiu4sZEDURXkBgDF8iAyRAgEAxAYExA63dxQyImggv4OXd4UtkgAQIECgmIDBmoLXzkgFRE00IePCliTIZJAECBLILCIwZSD8/PkzPt/z848noDKiaCCkgMIYsi0ERIECguIDAuJH40+PDy2kYfnYch2F8ur272dis0wmEFBAYQ5bFoAgQIFBcQGDcSHx+Ofrr7R3TjaZOjysgMMatjZERIECgpIBws0HXQwAb8JzapIDA2GTZDJoAAQKbBQTGlYRepbMSzmlNCwiMTZfP4AkQILBaQGBcSTf3Kh3f7LIS02nNCAiMzZTKQAkQIJBVQGBcyendiyvhnNa0gMDYdPkMngABAqsFBMaVdL5XdyWc05oWEBibLp/BEyBAYLWAwLiCzsMuK9Cc0oWAwNhFGU2CAAECyQICYzLZMPhmlxVoTulCQGDsoowmQYAAgWQBgTGZTGBcQeaUTgQExk4KaRoECBBIFBAYE8Gmw92/uALNKV0ICIxdlNEkCBAgkCwgMCaTvQ+MXqWzAtApzQoIjM2WzsAJECCwSUBgXMHnj+YKNKd0IWB3vYsymgQBAgSSBQTGZDI7jCvInNKJgAe+OimkaRAgQCBRQGBMBJsO//z4MF2J/vbjkvQKQKc0KyAwNls6AydAgMAmAYExke/T48PLaRh+dhuHYXy6vbtJbMbhBJoU8A7SJstm0AQIENgsIDAmEp7vsHy9vWOYaOjwtgXcw9t2/YyeAAECawSEnUQ1fywTwRzenYDfge5KakIECBC4KiAwXiV6f4A/lolgDu9OwO9AdyU1IQIECFwVEBivEgmMiUQO71zAq3U6L7DpESBAYEZAYExcFnZXEsEc3p2AJ6W7K6kJESBA4KqAwHiVyA5jIpHDOxcQGDsvsOkRIEDADuP2NWCHcbuhFtoW8Gqdtutn9AQIEFgjYIcxUU1gTARzeJcCfg+6LKtJESBA4KKAwJi4OPyhTARzeJcCfg+6LKtJESBAQGDMtQb8ocwlqZ2WBfwetFw9YydAgEC6gB3GRDN/KBPBHN6lgN+DLstqUgQIELDDmGsN+EOZS1I7LQv4PWi5esZOgACBdAE7jIlm/lAmgjm8SwG/B12W1aQIECBghzHXGvCHMpekdloW8HvQcvWMnQABAukCdhgTzfyhTARzeJcCvh6wy7KaFAECBOww5loDAmMuSe20LODbXlqunrETIEAgXcAOY6KZwJgI5vAuBc4D4zTJl3Ecn7/c33Q5YZMiQIDAwQUExsQFIDAmgjm8S4Hzrwd8neQ4DOM4joPg2GXZTYoAgQMLCIyJxRcYE8Ec3q3A3C7j62TtNnZbdhMjQOCgAgJjYuEFxkQwh3crcGmX8e1u4/T/23HsdgmYGAECBxIQGBOLLTAmgjm8a4EpNJ6mnyuznC5VvztkHIcn9zt2vTZMjgCBvgSufc73NdsMsxEYMyBqojuBa7uNcxOebnYUGrtbCiZEgECnAgJjYmEFxkQwhx9G4HW3cZrwkg+Wacvx6fZuyaGHMTRRAgQIRBXwYZ1YGYExEczhhxR4Gx5fAc4/bATGQy4NkyZAoFEBgTGxcL7hIhHM4QR+CHz6cb/jK4jAaGkQIECgHQGBMbFWvuEiEczhBN4I2KG3HAgQINCmgMCYWDeBMRHM4QQuBMbpf55eufP05d7nkFVCgACB4AI+qBMLdP40qMtqiYAOP7TA3Mu+hcZDLwmTJ0CgEQGBcUWh3Me4As0pBIZhmA2Mnpa2NggQIBBeQGBcUSKXpVegOYXAFBh/uh/nXvNtl9HyIECAQGwBgXFFfQTGFWhOIfBDYC40urXD8iBAgEBsAYFxRX3mvtXiZRzHZ191tkLTKUcU8I+uI1bdnAkQaFlAYFxZPX/wVsI5jcCFS9NffeuLtUGAAIGwAgLjytIIjCvhnEbgo0vTXrNjfRAgQCCkgMC4sixer7MSzmkE3gh8fnyYbl989+MBGEuEAAEC8QQExg018XqdDXhOJXDhNTsTjNBoeRAgQCCWgMC4oR4uS2/AcyqBj16z492M1geBIgLT1bG5V1sV6Sxjo9M/Ij1YmhF0RVMC4wq011PmXkL8Mgx/fr69+5sNzTqVwKEELr2b8e/+d/z7//yX+/8+FIbJElgp8Onx4WXJqadhaPbv/jgMs7ewCJJLKr/9mGYXzvapb29h7vU6U6svw/Cn59u7X23vQQsEjiEwFxo9NX2M2ptlmsDcDmHLITBt9vNHzwXJuSPtUm7TFhi3+c1+1dnU5DgMz0+3d582Nu90AocRON+xFxgPU/pmJ7rH5d3c4fAXW3aBqlEioFwLl0Ll5QVQoh6BllvaUNb+8s/9Ak+/hKdx/P0wDL8fTqfffb29e0gbjaMJHEtg2mUcTv//kfTkvYzHWgCFZ7v28/2jYeUObzkIUgLgGPwLJ37U7Bc5pXRwESrnV2Jp9xzrP2sbH31olPzlt1uStYwaI0AgmECJQJZziiU/33OOM7WtNwFxfLq9u0k9v8XjLwXJubmUCjmvoTLyjuTK38lpHf1VNctvOwVrfk6ndecl9LXXh4bAmFAkhxIgEE7g2h+fvT5bI0EV/wN2NtnoO4QRarMkXG4Nldd2JPdy2PI7OY7jy3CaHskY/nwahj8O4/D1ndPqoHem0eIj+3MFXfPL/wr6/ZL08IfhNEyXpadL0vd7LRr9Eogk8A///q//+F9/+p//mBvT05f7rZ/dkaYafizXQuDbCWz54xMRYs3n+0fzEN4iVnnZmGqEymUjiX3U6e2Hdy9BL4X80ofGml/+6bUGrx+q0784jnJ5IMXbsQQmgblveJn+9+nyzpYfgfO93rVAWDIEbqvkllVw/dw1n+/XW3VEzwJvQ2Wr/6q99jt5bV7f/vulD+9cxb82yFz9pLaT+0Pj0+PDtHX77dr/OAx/ebq9++vUMTmewBEESn3mJAXOuVtgvn+Xdfj7wK4Fwdc1tFcgzP3ZeoTfCXNsR2DJjmS02Sz9nfz008NfhtMwfQZO0e3bJemb6d/yw/CrDwNjlqD3/QP4WnCNZrtqPJ8eH/54Goa//REY//TkXYyrHJ3Uv8D0Cp1plhE/GKLej/R2VZQKgks/85f+8el/JZshgf4FPv/b/W+Gm9Nvvn1ev354v5v2gYJernJ/fnz4OnH+CIx/PL2Mv/362/vf5WpfOwR6Ezh/lU7q/CIGztQ51Dz+o0AoBNashL4ItCfg8zZjzT7/9PD74TT805smHzzskhFYUwTOBLYGzqi7nKmFXrIzKBCmqjqeAIGzKxtAcgl8fnyYdhP/WWDMJaodAuUFWrwf6a2KIFh+jeiBAIH3QxbbAAAAB0lEQVRh+D/f1umq8KvKSAAAAABJRU5ErkJggg==\",\"left\":10,\"top\":102,\"width\":652,\"height\":282,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"FreehandMarker\",\"state\":\"select\"},{\"color\":\"#10B981\",\"fontFamily\":\"Helvetica, Arial, sans-serif\",\"padding\":5,\"text\":\"clear line between nature and man made\",\"left\":291,\"top\":219,\"width\":372,\"height\":223,\"rotationAngle\":0,\"visualTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"containerTransformMatrix\":{\"a\":1,\"b\":0,\"c\":0,\"d\":1,\"e\":0,\"f\":0},\"typeName\":\"TextMarker\",\"state\":\"select\"}]}",
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
            work_1_marker_obj=comp.get("work_1_marker_obj"),
            work_2_marker_obj=comp.get("work_2_marker_obj"),
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
