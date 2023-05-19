from django.contrib.auth.base_user import BaseUserManager


class UserProfileManager(BaseUserManager):
    def create_user(self, username, email, first_name, is_staff, is_active, last_name, password="12345678"):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email)

        user.username = username
        user.email = email
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_staff = is_staff
        user.is_active = is_active
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password, name="superuser", role=1, photo=None)
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user
