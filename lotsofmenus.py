from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import CategoryItem, Base, Category, User

engine = create_engine('sqlite:///itemcatlouge.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Arslan Shakoor", email="sunbun@arslan.com",
             picture='')
session.add(User1)
session.commit()

# category for soccer
category1 = Category(user_id=1, name="Soccer")

session.add(category1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Nike Hypervenom Phantom III ", description="The next generation of deadly attacking is here with the Nike Hypervenom 3. Made for the lethal strikers who can cut, strike, and score, the new Hypervenom is perfect for the striker looking for goals. ",
                     price="$7.50", type="Sale", category=category1)

session.add(categoryItem2)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="adidas Mexico Home Jersey 2016", description="This is the official fan version of the jersey that El Tri will line up in while competing in the historic 2016 Copa America Centenario.",
                     price="$2.99", type="Available", category=category1)

session.add(categoryItem1)
session.commit()

categoryItem3 = CategoryItem(user_id=1, name="PUMA Team Jersey", description="Created for top level play, PUMA's Team kit not only looks professional on the field, it feels great too",
                     price="$5.50", type="Coming Soon", category=category1)

session.add(categoryItem3)
session.commit()

 

categoryItem4 = CategoryItem(user_id=1, name="Vici Futbol Maestro Soccer Ball", description="Designed to work with the Maestro Boot Cover to help players understand which part of the foot to use when striking the ball",
                     price="$7.99", type="Coming Soon", category=category1)

session.add(categoryItem4)
session.commit()

 

 


# category for cricket
category2 = Category(user_id=1, name="Cricket")

session.add(category2)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name=" Gunn & Moore 808 Batting Pads", description="Gunn and Moore have certainly excelled themselves in producing their 2017 range of batting pads, perfect for the modern day game and all its demands.",
                     price="$7.99", type="Sale", category=category2)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name=" Kookaburra Ghost",
                     description="Product innovation and quality is what makes Kookaburra produce excellent products year after year", price="$25", type="Available", category=category2)

session.add(categoryItem2)
session.commit()

# category for baseball
category3 = Category(user_id=1, name="Baseball")

session.add(category3)
session.commit()


categoryItem1 = CategoryItem(user_id=1, name="Easton E300T Bat Tote Bag", description=" Internal valuables pocket",
                     price="$8.99", type="Sale", category=category3)

session.add(categoryItem1)
session.commit()

categoryItem2 = CategoryItem(user_id=1, name="Wilson Sleek", description="Wilson Sleek Matte Finish Pro Skull Cap",
                     price="$6.99", type="Available", category=category3)

session.add(categoryItem2)
session.commit()


               

# category for basketball
category4 = Category(user_id=1, name="BasketBall")

session.add(category4)
session.commit()


# category for Tony's badminton
category5 = Category(user_id=1, name="Badminton")

session.add(category5)
session.commit()

# category for table tennis
category6 = Category(user_id=1, name="Table Tennis")

session.add(category6)
session.commit()

 
# category for ice hockey
category7 = Category(user_id=1, name="Ice Hockey")

session.add(category7)
session.commit()

# category for boxing
category8 = Category(user_id=1, name="Boxing")

session.add(category8)
session.commit()

# category for hockey
category9 = Category(user_id=1, name="Hockey")
session.add(category9)
session.commit()

 


 


print "added category items!"