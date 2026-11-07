import { prisma } from "./db.js";

try {
  const users = await prisma.user.findMany();
  console.log(users);
} finally {
  await prisma.$disconnect();
}
