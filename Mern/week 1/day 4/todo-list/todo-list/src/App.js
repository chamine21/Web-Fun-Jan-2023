import './App.css';
import React, { useState } from 'react';

function TodoList() {
  const [tasks, setTasks] = useState([]);

  const handleAddTask = (text) => {
    const newTask = {
      text: text,
      completed: false
    };
    setTasks([...tasks, newTask]);
  };

  const handleToggleTask = (index) => {
    setTasks((prevTasks) => {
      const updatedTasks = [...prevTasks];
      updatedTasks[index].completed = !updatedTasks[index].completed;
      return updatedTasks;
    });
  };

  const handleRemoveTask = (index) => {
    setTasks((prevTasks) => prevTasks.filter((_, i) => i !== index));
  };

  return (
    <div>
      <h2>Todo List</h2>
      <form onSubmit={(e) => {
        e.preventDefault();
        const text = e.target.task.value;
        if (text) {
          handleAddTask(text);
          e.target.task.value = '';
        }
      }}>
        <input type="text" name="task" placeholder="Add new task" />
        <button type="submit">Add</button>
      </form>
      <ul>
        {tasks.map((task, index) => (
          <li
            key={index}
            style={{ textDecoration: task.completed ? 'line-through' : 'none' }}
            onClick={() => handleToggleTask(index)}
          >
            {task.text}
            <button onClick={() => handleRemoveTask(index)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TodoList;

