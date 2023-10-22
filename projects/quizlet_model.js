// Install the necessary packages using:
// npm install express mongoose bcrypt jsonwebtoken

// server.js
const express = require('express');
const mongoose = require('mongoose');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const app = express();
const PORT = process.env.PORT || 3000;

// MongoDB connection
mongoose.connect('mongodb://localhost:27017/quizlet', { useNewUrlParser: true, useUnifiedTopology: true });
const db = mongoose.connection;

db.on('error', console.error.bind(console, 'MongoDB connection error:'));
db.once('open', () => {
  console.log('Connected to MongoDB');
});

// Define mongoose schema and model for users
const userSchema = new mongoose.Schema({
  username: { type: String, unique: true, required: true },
  password: { type: String, required: true },
});

const User = mongoose.model('User', userSchema);

// Define mongoose schema and model for study materials
const studyMaterialSchema = new mongoose.Schema({
  title: { type: String, required: true },
  content: { type: String, required: true },
});

const StudyMaterial = mongoose.model('StudyMaterial', studyMaterialSchema);

app.use(express.json());

// Authentication middleware
function authenticateToken(req, res, next) {
  const token = req.header('Authorization');
  if (!token) return res.sendStatus(401);

  jwt.verify(token, 'secretKey', (err, user) => {
    if (err) return res.sendStatus(403);
    req.user = user;
    next();
  });
}

// Register a new user
app.post('/register', async (req, res) => {
  try {
    const hashedPassword = await bcrypt.hash(req.body.password, 10);
    const user = new User({ username: req.body.username, password: hashedPassword });
    await user.save();
    res.status(201).send('User registered successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error registering user');
  }
});

// Login and generate JWT token
app.post('/login', async (req, res) => {
  const user = await User.findOne({ username: req.body.username });
  if (!user) return res.status(401).send('Invalid username or password');

  const validPassword = await bcrypt.compare(req.body.password, user.password);
  if (!validPassword) return res.status(401).send('Invalid username or password');

  const token = jwt.sign({ username: user.username }, 'secretKey');
  res.header('Authorization', token).send('Login successful');
});

// Create a new study material
app.post('/study-material', authenticateToken, async (req, res) => {
  try {
    const studyMaterial = new StudyMaterial({ title: req.body.title, content: req.body.content });
    await studyMaterial.save();
    res.status(201).send('Study material created successfully');
  } catch (error) {
    console.error(error);
    res.status(500).send('Error creating study material');
  }
});

// Get all study materials
app.get('/study-materials', async (req, res) => {
  try {
    const studyMaterials = await StudyMaterial.find();
    res.json(studyMaterials);
  } catch (error) {
    console.error(error);
    res.status(500).send('Error getting study materials');
  }
});

// Start the server
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
