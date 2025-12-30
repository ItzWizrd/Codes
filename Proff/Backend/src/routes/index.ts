import { Router } from "express";
import { todo } from "node:test";

const app = Router();
app.post("/create",TodoController.createTodo);
export default app;