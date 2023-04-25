import tensorflow as tf


def wrap_frozen_graph(graph_def, inputs, outputs):
    def _imports_graph_def():
        tf.compat.v1.import_graph_def(graph_def, name="")

    wrapped_import = tf.compat.v1.wrap_function(_imports_graph_def, [])
    import_graph = wrapped_import.graph

    return wrapped_import.prune(
        tf.nest.map_structure(import_graph.as_graph_element, inputs),
        tf.nest.map_structure(import_graph.as_graph_element, outputs))

with tf.io.gfile.GFile("/home/samin/Documents/existing/yolov5/runs/train/exp56/weights/best.pt", "rb") as f:
    graph_def = tf.compat.v1.GraphDef()
    loaded = graph_def.ParseFromString(f.read())
    frozen_func = wrap_frozen_graph(graph_def=graph_def,
                                    inputs=["images:0"],
                                    outputs=['output:0','424:0', '444:0'])
    converter = tf.lite.TFLiteConverter.from_concrete_functions([frozen_func])
    # converter.allow_custom_ops = True
    # converter.experimental_new_converter = True
    converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS, tf.lite.OpsSet.SELECT_TF_OPS]
    converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tf_lite_model = converter.convert()
    open('/home/samin/Documents/existing/yolov5/runs/train/exp56/weights/best.tflite', 'wb').write(tf_lite_model)