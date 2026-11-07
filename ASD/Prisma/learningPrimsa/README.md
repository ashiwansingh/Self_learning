# Prisma learning project

This project uses Prisma ORM 7, JavaScript, and PostgreSQL.

## Get started

1. Install dependencies with `npm install`.
2. Set `DATABASE_URL` in `.env` to your PostgreSQL connection string (see `.env.example` for the format).
3. Generate Prisma Client with `npm run db:generate`.
4. Apply the schema to your development database with `npm run db:migrate -- --name init`.
5. Run the example query with `npm start`.

The starter schema defines a `User` model in `prisma/schema.prisma`. Use
`npm run db:studio` to inspect the database in Prisma Studio.
