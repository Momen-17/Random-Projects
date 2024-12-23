import 'package:first_project/widgets/confirm_delete_dialog.dart';
import 'package:flutter/material.dart';
import 'package:flutter_slidable/flutter_slidable.dart';
import 'package:provider/provider.dart';
import '../providers/task_provider.dart';

class DeletedTasksScreen extends StatelessWidget {
  const DeletedTasksScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final taskProvider = Provider.of<TaskProvider>(context);
    final deletedTasks = 
      taskProvider.tasks.where((task) => task.isDeleted).toList();

    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const Text(
          'Deleted Tasks',
          style: TextStyle(fontSize: 24),
        ),
      ),
      body: deletedTasks.isEmpty
          ? const Center(
              child: Text(
                'Trash is empty.',
                style: TextStyle(fontSize: 18, color: Colors.grey),
              ),
            )
          : Column(
              children: [
                Expanded(
                  child: ListView.builder(
                    itemCount: deletedTasks.length,
                    itemBuilder: (context, index) {
                      final task = deletedTasks[index];
                      return Padding(
                        padding: const EdgeInsets.symmetric(
                            horizontal: 10.0, vertical: 5.0),
                        child: Slidable(
                          key: Key(task.id),
                          direction: Axis.horizontal,
                          endActionPane: ActionPane(
                            motion: const StretchMotion(),
                            extentRatio: 0.25,
                            children: [
                              SlidableAction(
                                onPressed: (context) {
                                  showConfirmDeleteDialog(context, task.id);
                                },
                                backgroundColor: Colors.red,
                                foregroundColor: Colors.white,
                                icon: Icons.delete_forever,
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
                              title: Text(task.title),
                              trailing: IconButton(
                                icon: const Icon(Icons.restore,
                                    color: Colors.green),
                                onPressed: () {
                                  taskProvider.toggleDelete(task.id); // Restore task
                                },
                              ),
                            ),
                          ),
                        ),
                      );
                    },
                  ),
                ),
                Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: ElevatedButton.icon(
                    onPressed: () {
                      taskProvider.clearDeletedTasks(); // Clear all tasks
                      ScaffoldMessenger.of(context).showSnackBar(
                        const SnackBar(
                          content: Text('Trash emptied!'),
                          duration: Duration(seconds: 1),
                        ),
                      );
                    },
                    icon: const Icon(Icons.delete_sweep),
                    label: const Text('Empty Trash'),
                    style: ElevatedButton.styleFrom(
                      foregroundColor: Colors.white, backgroundColor: Colors.red,
                    ),
                  ),
                ),
              ],
            ),
    );
  }
}
