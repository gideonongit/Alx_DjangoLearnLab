# 📚 LibraryProject – Advanced Features and Security

This Django project demonstrates advanced user management features including a custom user model and a role-based access control system using permissions and groups.

---

## 🔐 Custom User Model

We use a custom user model `CustomUser` defined in `bookshelf/models.py`, which extends `AbstractUser` to include:

- `date_of_birth`: A `DateField`
- `profile_photo`: An `ImageField`

### ➕ How to Add Users
Users can register through a registration form using Django's built-in `UserCreationForm`.

---

## 👥 User Groups and Permissions

We manage user access through Django groups and custom permissions defined on the `Document` model.

### 🛡️ Defined Permissions:
- `can_view`: View a document
- `can_create`: Create a new document
- `can_edit`: Edit an existing document
- `can_delete`: Delete a document

### 👥 Groups:
- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_create`, `can_edit`
- **Admins**: Assigned all permissions

Groups and permissions can be automatically set up using the management command:

```bash
python manage.py setup_groups
