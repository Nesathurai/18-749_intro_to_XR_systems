from arena import *
scene = Scene(host="arenaxr.org", scene="scene")

def click_handler(scene, evt, msg):
	print(evt.type)
	mybox = Box(object_id="my_box",
	position=(0,2,-3),
	scale=(0.25,0.25,0.25),
	color=(50,60,200),
	evt_handler=click_handler,)
	if(evt.type == "mouseenter"): # == "buttonClick", "mousedown", "mouseup", "mouseenter", "mouseleave", etc.
		scene.add_object(mybox)
		# open_eye_morph = [Morph(morphtarget="abc",value=0.0), Morph(morphtarget="def",value=1.0)]
		# xr_logo.update_morph(open_eye_morph)
		# scene.update_object(xr_logo)
		xr_logo.dispatch_animation(AnimationMixer(clip="*", loop="once"))
		scene.run_animations(xr_logo)

	if(evt.type=="mouseleave"):
		scene.delete_object(mybox)

@scene.run_once
def make_box():
	global xr_logo
	xr_logo = GLTF(
        object_id="xr-logo",
        position=(0,0,-3),
        scale=(1.2,1.2,1.2),
        url="/store/users/anesathu/handAnim.glb",
		evt_handler=click_handler,
		clickable=True,
		persist=True
    )
	scene.add_object(xr_logo)


scene.run_tasks()