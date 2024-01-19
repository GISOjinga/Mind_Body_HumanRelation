import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class CognitiveFunction(Base):
    __tablename__ = 'cognitive_function'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Emotion(Base):
    __tablename__ = 'emotion'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)

class MemoryLearning(Base):
    __tablename__ = 'memory_learning'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class BodyComposition(Base):
    __tablename__ = 'body_composition'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class FunctionalAbility(Base):
    __tablename__ = 'functional_ability'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class PhysiologicalAspect(Base):
    __tablename__ = 'physiological_aspect'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class SensoryPerception(Base):
    __tablename__ = 'sensory_perception'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class MindBodyRelation(Base):
    __tablename__ = 'mind_body_relation'
    id = Column(Integer, primary_key=True)
    cognitive_function_id = Column(Integer, ForeignKey('cognitive_function.id'))
    emotion_id = Column(Integer, ForeignKey('emotion.id'))
    memory_learning_id = Column(Integer, ForeignKey('memory_learning.id'))
    body_composition_id = Column(Integer, ForeignKey('body_composition.id'))
    functional_ability_id = Column(Integer, ForeignKey('functional_ability.id'))
    physiological_aspect_id = Column(Integer, ForeignKey('physiological_aspect.id'))
    sensory_perception_id = Column(Integer, ForeignKey('sensory_perception.id'))

    cognitive_function = relationship(CognitiveFunction)
    emotion = relationship(Emotion)
    memory_learning = relationship(MemoryLearning)
    body_composition = relationship(BodyComposition)
    functional_ability = relationship(FunctionalAbility)
    physiological_aspect = relationship(PhysiologicalAspect)
    sensory_perception = relationship(SensoryPerception)

    def to_dict(self):
        return {
            'cognitive_function_id': self.cognitive_function_id,
            'emotion_id': self.emotion_id,
            'memory_learning_id': self.memory_learning_id,
            'body_composition_id': self.body_composition_id,
            'functional_ability_id': self.functional_ability_id,
            'physiological_aspect_id': self.physiological_aspect_id,
            'sensory_perception_id': self.sensory_perception_id
        }

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
