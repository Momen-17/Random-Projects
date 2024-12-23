import 'package:first_project/widgets/edit_task_dialog.dart';
import 'package:flutter/material.dart';
import 'package:flutter_slidable/flutter_slidable.dart';
import 'package:provider/provider.dart';
import '../providers/task_provider.dart';

class PendingTasksScreen extends StatelessWidget {
  const PendingTasksScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final taskProvider = Provider.of<TaskProvider>(context);
    final pendingTasks =
        taskProvider.tasks.where((task) => !task.isCompleted && !task.isDeleted).toList();

    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text(
          'Pending Tasks',
          style: TextStyle(fontSize: 24),
        ),
      ),
      body: pendingTasks.isEmpty
          ? const Center(
              child: Text(
                'No pending tasks yet.',
                style: TextStyle(fontSize: 18, color: Colors.grey),
              ),
            )
          : ListView.builder(
              itemCount: pendingTasks.length,
              itemBuilder: (context, index) {
                final task = pendingTasks[index];
                return Padding(
                  padding: const EdgeInsets.symmetric(
                      horizontal: 10.0, vertical: 5.0),
                  child: Slidable(
                    key: Key(task.id), // Unique key for each task
                    direction: Axis.horizontal, // Enable horizontal swipe
                    endActionPane: ActionPane(
                      motion: const StretchMotion(), // Smooth stretch motion
                      extentRatio: 0.25, // Smaller swipe size (25% of the width)
                      children: [
                        SlidableAction(
                          onPressed: (context) {
                            taskProvider.toggleDelete(task.id); // Delete task
                            ScaffoldMessenger.of(context).showSnackBar(
                              const SnackBar(
                                content: Text('Task moved to trash'),
                                duration: Duration(seconds: 1),
                              ),
                            );
                          },
                          backgroundColor: Colors.red,
                          foregroundColor: Colors.white,
                          icon: Icons.delete,
                          label: 'Delete',
                        ),
                      ],
                    ),
                    child: Card(
                      elevation: 3,
                      shape: RoundedRectangleBorder(
                        borderRadius: BorderRadius.circular(10.0),
                      ),
                      child: ListTile(
                        leading: Checkbox(
                          value: task.isCompleted,
                          onChanged: (_) {
                            taskProvider.toggleComplete(task.id); // Uncheck task
                          },
                        ),
                        title: Text(
                          task.title,
                          style: TextStyle(
                            color: task.isImportant
                              ? Colors.blue
                              : Theme.of(context).textTheme.bodyLarge?.color,
                          ),
                        ),
                        trailing: Row(
                          mainAxisSize: MainAxisSize.min,  
                          children: [
                            IconButton(
                              icon: const Icon(Icons.edit, color: Colors.blueGrey),
                              onPressed: () =>
                                  showEditTaskDialog(context, task.id, task.title),
                            ),
                            IconButton(
                              icon: Icon(task.isImportant ? Icons.star : Icons.star_border, color: Colors.blue),
                              onPressed: () => 
                                taskProvider.toggleImportant(task.id),
                                
                            ),
                          ],
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
    );
  }
}
