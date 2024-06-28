
# Django Dashboards

## Pré-requisitos

1. **Verificar o `pg_hba.conf` e `postgresql.conf`**

   Se o banco de dados antigo estiver rodando na sua máquina local, certifique-se de que o PostgreSQL está configurado para permitir conexões no banco de dados antigos.

   ### Editar `pg_hba.conf`

   Adicione a linha para permitir conexões de todas as redes:

   ```conf
   # Localhost e IPv4 locais
   host    all             all             127.0.0.1/32            md5
   host    all             all             ::1/128                 md5

   # Rede específica
   host    all             all             0.0.0.0/0               md5
   ```

   ### Editar `postgresql.conf`

   Habilite escuta em todos os endereços IP:

   ```conf
   listen_addresses = '*'
   ```

2. **Configurar o arquivo `.env`**

   Modifique ou crie o arquivo `.env` no diretório `/django_project` (mesmo diretório que está o arquivo `manage.py` ) com as seguintes informações para acessar o banco de dados antigo:

   ```env
   SECRET_KEY='sua_chave_secreta'
   DEBUG=True

   OLD_DB_NAME='nome_do_banco'
   OLD_DB_USER='usuario_do_banco'
   OLD_DB_PASSWORD='senha_do_banco'
   OLD_DB_HOST='endereco_do_banco'
   OLD_DB_PORT=5432
   ```
   Caso o banco esteja em sua máquina local utilize seu endereço IP interno.
   No Linux é possível visualizar este IP com o comando:
   ```bash
   hostname -I
   ```

## Instruções de Instalação

1. **Clonar o Repositório**

   ```bash
   git clone https://github.com/teuzin112/django-dashboards.git
   cd django-dashboards
   ```

2. **Iniciar os Contêineres Docker**

   ```bash
   docker compose up
   ```

3. **Acessar o Contêiner Django**

   Em outro terminal, acesse o contêiner Django para realizar as migrações e criar um superusuário:

   ```bash
   docker exec -it django_gunicorn sh
   ```

4. **Criar um Superusuário**

   Dentro do contêiner, crie um superusuário para acessar a página de administração:

   ```bash
   python manage.py createsuperuser
   ```

5. **Aplicar Migrações**

   Ainda dentro do contêiner, aplique as migrações:

   ```bash
   python manage.py migrate
   ```

## Realizar migração dos dados
1. **Acesse o container django**
```bash
docker exec -it django_gunicorn sh
```

2. **Realize os comandos:**
```bash
python manage.py migrate_data
```
```bash
python manage.py migrate_nit
```

## Acessar a Aplicação

- A aplicação estará disponível em `http://localhost:8008`.
- Acesse a página de administração em `http://localhost:8008/admin` usando o superusuário criado.
- Caso queira também possui um PgAdmin rodando no `http://localhost:8001` com usuário `admin@admin.com` e senha `admin`.
