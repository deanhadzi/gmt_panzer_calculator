from db import engine
import model

model.Base.metadata.create_all(engine)
