from visdom import Visdom
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
# from detectron2.engine import  HookBase

class VisdomPlotter(object):
    """Plots to Visdom"""
    def __init__(self, env_name='main'):
        # self.viz = Visdom(log_to_filename=os.path.join("./logs", env_name+"_visdom"), offline=True) #
        self.viz = Visdom(server='http://10.141.1.179')
        self.env = env_name
        self.plots = {}


    # def after_step(self):
    #     if (self.trainer.iter + 1)% self._period == 0 or (self.trainer.iter === self.trainer.max_iter - 1):
    #         self.plot()

    def plot(self, var_name, split_name, title_name, x, y):
    # def plot(self):
        # var_name = self.trainner.var_name
        # split_name = self.split_name
        # title_name = self.trainer.var_name
        # x = self.trainer.iter_step
        # y = self.trainer.var_value


        if var_name not in self.plots:
            self.plots[var_name] = self.viz.line(X=np.array([x,x]), Y=np.array([y,y]), env=self.env, opts=dict(
                legend=[split_name],
                title=title_name,
                xlabel='Steps',
                ylabel=var_name
            ))
            # self.plots[var_name] = self.viz.line(X=np.array([x,x]), Y=np.array([y,y]), opts=dict(
            #     legend=[split_name],
            #     title=title_name,
            #     xlabel='Epochs',
            #     ylabel=var_name
            # ))


            # save_file = os.path.join("./logs", self.env, "%s.png"%(var_name))
            # plt.plot(np.array([x,x]), np.array([y,y]))
            # # plt.show()
            # plt.savefig(save_file)

        else:
            self.viz.line(X=np.array([x]), Y=np.array([y]), env=self.env, win=self.plots[var_name], name=split_name, update = 'append')
            # self.viz.line(X=np.array([x]), Y=np.array([y]), win=self.plots[var_name], name=split_name, update = 'append')
            # save_file = os.path.join("./logs", self.env, "%s.png"%(var_name))
            # plt.plot(np.array([x,x]), np.array([y,y]))
            # # plt.show()
            # plt.savefig(save_file)

# # output_dir: logs/
#     def save(self):
#         for key, plot in self.plots.items():
#             save_file = os.path.join("./logs", self.env, "%s.png"%(key))
#
#             cv2.imwrite(save_file, plot)
