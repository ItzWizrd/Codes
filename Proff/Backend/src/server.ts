import express from 'express';
import cors from 'cors';

const app = express();
const PORT = process.env.PORT || 3000;
app.use(
    cors({
        origin: 'http://localhost:5173/',
        methods: ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'],
        credentials: true,
        allowedHeaders: ['Content-Type', 'Authorization'],
    })
);


app.get("/health", (req, res) => {
    res.status(200).send("Server is healthy");
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});