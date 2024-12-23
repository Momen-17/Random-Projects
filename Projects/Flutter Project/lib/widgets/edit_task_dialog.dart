import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/task_provider.dart';

void showEditTaskDialog(BuildContext context, String taskId, String currentTitle) {
  final TextEditingController controller = TextEditingController(text: currentTitle);

  showDialog(
    context: context,
    builder: (context) {
      return AlertDialog(
        title: const Text('Edit Task'),
        content: TextField(
          controller: controller,
          autofocus: true,
          decoration: const InputDecoration(hintText: 'Task Title'),
        ),
        actions: [
          TextButton(
            onPressed: () {
              Navigator.pop(context); // Close dialog without saving
            },
            child: const Text('Cancel'),
          ),
          TextButton(
            onPressed: () {
              final newTitle = controller.text.trim();
              if (newTitle.isNotEmpty) {
                Provider.of<TaskProvider>(context, listen: false)
                    .updateTask(taskId, newTitle);
              }
              Navigator.pop(context); // Close dialog after saving
            },
            child: const Text('Save'),
          ),
        ],
      );
    },
  );
}
