from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

# Models

# User, class?/date?, TODO decide between teacher submitting class stats with 
# students copying stats or have students do it manually as is done now
# with option 1, still need date for students to submit extra training done at home