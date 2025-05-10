const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());
app.use(express.json());

let comments = [];
let bannedUsers = [];

app.post('/check', (req, res) => {
  const { userId, comment } = req.body;
  const toxicWords = ['hate', 'idiot', 'stupid'];
  const isToxic = toxicWords.some(word => comment.toLowerCase().includes(word));

  const newComment = {
    id: comments.length + 1,
    userId,
    comment,
    isToxic
  };

  comments.push(newComment);
  res.json(newComment);
});

app.get('/admin/comments', (req, res) => {
  res.json(comments);
});

app.delete('/admin/comment/:id', (req, res) => {
  const id = parseInt(req.params.id);
  comments = comments.filter(comment => comment.id !== id);
  res.send({ message: "Comment deleted" });
});

app.post('/admin/ban', (req, res) => {
  const { userId } = req.body;
  bannedUsers.push(userId);
  res.send({ message: `User ${userId} banned.` });
});

app.listen(PORT, () => {
  console.log(`🚀 Server running at http://localhost:${PORT}`);
});