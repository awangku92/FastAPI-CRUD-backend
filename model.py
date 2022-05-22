# import config as conf
from db.db import s, Base
from db.user import User
from db.schemas import UserIn, UserOut
import logging, os, json

project_root = os.path.join(os.path.dirname(__file__), 'logs') 

class CRUD():
    def create_user(usermodel):
        try:
            user = User(name = usermodel.name, phoneno = usermodel.phoneno)
            s.add(user)
            s.commit()
            s.refresh(user)

            # # get the id given to the object from the database
            # uid = user.id

        except Exception as e:
            logging.basicConfig(filename=project_root+'\\create_user.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.error(e)
            logging.shutdown()
            s.rollback()

            return str(e)

        s.close()
        return f'Success creating user with id : {user.id}!'

    def read_user(uid):
        try:
            user = s.query(User).get(uid)
            if user is None:
                return None

        except Exception as e:
            logging.basicConfig(filename=project_root+'\\read_user.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.error(e)
            logging.shutdown()
            s.rollback()

            return str(e)

        s.close()
        return  user

    def read_all_user():
        try:
            users_list = s.query(User).all()

        except Exception as e:
            logging.basicConfig(filename=project_root+'\\read_all_user.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.error(e)
            logging.shutdown()
            s.rollback()

            return str(e)

        s.close()
        return users_list

    def edit_user(uid, name, phoneno):
        try:
            user = s.query(User).get(uid)

            if user:
                user.name = name  
                user.phoneno = phoneno

                s.commit()
                s.refresh(user) # to get last session
            else:
                return None

        except Exception as e:
            logging.basicConfig(filename=project_root+'\\edit_user.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.error(e)
            logging.shutdown()
            s.rollback()

            return str(e)

        s.close()
        return user

    def delete_user(uid):
        try:
            user = s.query(User).get(uid)

            if user:
                s.delete(user)
                s.commit()
            else:
                return None

        except Exception as e:
            logging.basicConfig(filename=project_root+'\\delete_user.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            logging.error(e)
            logging.shutdown()
            s.rollback()

            return str(e)

        s.close()
        return {'detail':'User deleted!'}