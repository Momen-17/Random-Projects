import 'package:first_project/widgets/edit_task_dialog.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import '../providers/task_provider.dart';
import '../widgets/drawer_menu.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_slidable/flutter_slidable.dart';

class GradientText extends StatelessWidget {
  final String text;
  final Gradient gradient;

  const GradientText({
    super.key,
    required this.text,
    required this.gradient,
  });

  @override
  Widget build(BuildContext context) {
    return ShaderMask(
      shaderCallback: (bounds) => gradient.createShader(
        Rect.fromLTWH(0, 0, bounds.width, bounds.height),
      ),
      child: Text(
        text,
        style: GoogleFonts.pacifico( // Custom font
          fontSize: 36.0,
          fontWeight: FontWeight.bold,
          color: Colors.white, // This color will be replaced by the gradient
          shadows: [
            Shadow(
              blurRadius: 10.0,
              color: Colors.black.withOpacity(0.25),
              offset: const Offset(3.0, 3.0),
            ),
          ],
        ),
      ),
    );
  }
}

class HomeScreen extends StatefulWidget {
  final bool isDarkMode;
  final VoidCallback toggleTheme;

  const HomeScreen({
    super.key,
    required this.isDarkMode,
    required this.toggleTheme,
  });

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  final TextEditingController _controller = TextEditingController();
  final FocusNode _focusNode = FocusNode();

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _focusNode.requestFocus();
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    _focusNode.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final taskProvider = Provider.of<TaskProvider>(context);
    final allTasks =
      taskProvider.tasks.where((task) => !task.isDeleted).toList();

    return Scaffold(
      appBar: AppBar(
        centerTitle: true,
        title: const GradientText(
          text: 'ToDo',
          gradient: LinearGradient(
            colors: [Colors.blue, Colors.purple, Colors.red],
            begin: Alignment.topLeft,
            end: Alignment.bottomRight,
          ),
        ),
        leading: Builder(
          builder: (context) {
            return IconButton(
              icon: const Icon(Icons.menu),
              onPressed: () {
                Scaffold.of(context).openDrawer();
              },
            );
          },
        ),
        actions: [
          IconButton(
            icon: Icon(widget.isDarkMode ? Icons.dark_mode : Icons.light_mode),
            onPressed: () {
              widget.toggleTheme();
              WidgetsBinding.instance.addPostFrameCallback((_) {
                _focusNode.requestFocus();
              });
            },
          ),
        ],
      ),
      drawer: const DrawerMenu(),
      onDrawerChanged: (isOpen) {
        if (!isOpen) {
          // Refocus when the drawer is closed
          WidgetsBinding.instance.addPostFrameCallback((_) {
            _focusNode.requestFocus();
          });
        }
      },
      body: Column(
        children: [
          // Task List
          Expanded(
            child: ListView.builder(
              itemCount: allTasks.length,
              itemBuilder: (context, index) {
                final task = allTasks[index];
                return Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 10.0, vertical: 5.0),
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
                          onChanged: (value) {
                            taskProvider.toggleComplete(task.id);
                          },
                        ),
                        title: Text(
                          task.title,
                          style: TextStyle(
                            color: task.isImportant
                              ? Colors.blue
                              : Theme.of(context).textTheme.bodyLarge?.color,
                            decoration: task.isCompleted
                              ? TextDecoration.lineThrough
                              : TextDecoration.none,
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
            )
          ),

          // Add Task Field at Bottom
          Container(
            padding: const EdgeInsets.all(45.0),
            color: Theme.of(context).cardColor,
            child: Row(
              children: [
                // Text Field
                Expanded(
                  child: TextField(
                    controller: _controller,
                    focusNode: _focusNode,
                    decoration: const InputDecoration(
                      hintText: 'Add a task',
                      border: OutlineInputBorder(),
                    ),
                  ),
                ),
                const SizedBox(width: 8.0),

                IconButton(
                  icon: const Icon(Icons.add, color: Colors.blue),
                  onPressed: () {
                    final title = _controller.text.trim();
                    if (title.isNotEmpty) {
                      taskProvider.addTask(title);
                      _controller.clear();
                      _focusNode.requestFocus(); // Re-focus after adding
                    }
                  },
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
