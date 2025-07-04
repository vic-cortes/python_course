from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator, validator


class Usuario(BaseModel):
    """
    # Title Pydantic Example

    Modelo de usuario que valida los campos:
    - nombre: debe tener al menos 2 caracteres y estar en formato título.
    - email: debe ser un email válido.
    - edad: debe ser un entero entre 0 y 150.
    - activo: booleano que indica si el usuario está activo (por defecto True).
    """

    nombre: str
    email: EmailStr
    edad: Optional[int] = None
    activo: bool = True

    @field_validator("edad")
    @classmethod
    def validar_edad(cls, v):
        if v < 0 or v > 150:
            raise ValueError("La edad debe estar entre 0 y 150 años")
        return v

    @field_validator("nombre")
    @classmethod
    def validar_nombre(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres")
        return v.strip().title()


# Ejemplo de uso
if __name__ == "__main__":
    # Crear usuario válido
    usuario = Usuario(nombre="juan pérez", email="juan@ejemplo.com", edad=25)

    print(f"Usuario creado: {usuario}")
    print(f"Email: {usuario.email}")
    print(f"Nombre: {usuario.nombre}")

    # Convertir a JSON
    print(f"\nJSON: {usuario.model_dump_json()}")

    # Intentar crear usuario inválido
    try:
        usuario_invalido = Usuario(nombre="A", email="email-invalido", edad=200)
    except Exception as e:
        print(f"\nError de validación: {e}")
