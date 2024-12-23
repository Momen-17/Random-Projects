import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import '../models/task.dart';

class TaskProvider extends ChangeNotifier {
  final Box<Task> taskBox;

  TaskProvider(this.taskBox);

  List<Task> get tasks => taskBox.values.toList();

  void addTask(String title) {
    final task = Task(
      id: DateTime.now().toString(),
      title: title,
      isCompleted: false,
      isImportant: false,
      isDeleted: false,
    );
    taskBox.put(task.id, task);
    notifyListeners();
  }

  void toggleComplete(String id) {
    final task = taskBox.get(id);
    if (task != null) {
      final updatedTask = task.copyWith(isCompleted: !task.isCompleted);
      taskBox.put(id, updatedTask);
      notifyListeners();
    }
  }

  void toggleImportant(String id) {
    final task = taskBox.get(id);
    if (task != null) {
      final updatedTask = task.copyWith(isImportant: !task.isImportant);
      taskBox.put(id, updatedTask);
      notifyListeners();
    }
  }

  void toggleDelete(String id) {
    final task = taskBox.get(id);
    if (task != null) {
      final updatedTask = task.copyWith(isDeleted: !task.isDeleted);
      taskBox.put(id, updatedTask);
      notifyListeners();
    }
  }

  void updateTask(String id, String newTitle) {
    final task = taskBox.get(id);
    if (task != null) {
      final updatedTask = task.copyWith(title: newTitle);
      taskBox.put(id, updatedTask);
      notifyListeners();
    }
  }

  void deleteTask(String id) {
    taskBox.delete(id);
    notifyListeners();
  }

  void clearDeletedTasks() {
    final deletedTasksIds = taskBox.values
      .where((task) => task.isDeleted)
      .map((task) => task.id)
      .toList();
    
    for (String id in deletedTasksIds) {
      taskBox.delete(id);
    }
    notifyListeners();
  }
}
