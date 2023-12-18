from sqlalchemy.orm import relationship

class Company(Base):
    __tablename__ = 'companies'

    # existing columns

    def give_freebie(self, dev, item_name, value):
        freebie = Freebie(dev=dev, company=self, item_name=item_name, value=value)
        session.add(freebie)
        session.commit()

    @classmethod
    def oldest_company(cls):
        return session.query(cls).order_by(cls.founding_year).first()

    def freebies(self):
        return self.freebies

    def devs(self):
        return [freebie.dev for freebie in self.freebies]

