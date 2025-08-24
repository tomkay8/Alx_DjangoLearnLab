# Permissions and Groups Setup

- Custom permissions for Book model:
  - can_view
  - can_create
  - can_edit
  - can_delete

- Groups:
  - Viewers → can_view
  - Editors → can_view, can_create, can_edit
  - Admins → can_view, can_create, can_edit, can_delete

- Views use @permission_required decorators to enforce permissions.

