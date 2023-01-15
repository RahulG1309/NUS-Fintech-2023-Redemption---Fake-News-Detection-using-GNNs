# Redemption

For the NUS Fintech Month Hackathon 2023, our team presents **Redemption** a Fake News Detection as a Service, built with the State-Of-The-Art User Preference Aware GNNs. Our innovative approach leverages both intrinsic information of the news article in combination with exrtinsic information such as the User Propagation Graph to provide a highly accurate classifier for weaning out fake news articles.

## Product Description

In this project we harness the power of **Graph Neural Networks (GNNs)** for solving the problem of Fake News Detection. We utilise information regarding both the spread of fake news over Twitter via propogation graphs and the user preferences via past tweets to make a prediction about the veracity of a web article. This pipeline would most certainly provide business value as many organizations utilise news to help make business decisons.

![alt text](https://github.com/DChops/PayBack/blob/main/Graph.png?raw=true)

## Repository Structure

Before installation, here's an overview of the repository structure. It consists of 3 main sub directories.

<ol>
  <li> Components - This directory contains all the individual components used in the pipeline. Namely the graph generator, encoder, GNN model and driver script. This folder would be useful if one wishes to explore how a specific component works as they are thouroughly documented. </li>
  <li> Pipeline - This directory contains a compiled jupyter notebook of the end-to-end detection pipeline. We recommend checking this out as it would allow one to experiment with our service and see how the data flows from URL to propogation graph and finally an encoded tensor. It is also useful for experimenting with extensions/modifications to the service. </li>
  <li> REST API - This directory contains a Django project of a simple web application showcasing our Fake News Detector. Leveraging the Django REST Framework we created an API for our service and deployed it on Python Anywhere. The components used in the repository are the same ones found in /Components, but are resturctured in acccordance to the Django framework.</li>
</ol>

## Usage

One may acceess our online webapp at: http://redemption-paybackdelphi.pythonanywhere.com/

Alternatively, you could interact with the pipeline in a notebook environment found in _/Pipeline_.

## Datasets

We used the **Politifact** & **Gossicop** Datasets available publicly from the UPFD class in _*pytorch_geometric.datasets*_.

A brief summary of the datasets is as follows:
| Data | #Graphs | #Fake News| #Total Nodes | #Total Edges | #Avg. Nodes per Graph |
|-------|--------|--------|--------|--------|--------|
| Politifact | 314 | 157 | 41,054 | 40,740 | 131 |
| Gossipcop | 5464 | 2732 | 314,262 | 308,798 | 58 |

Both Politfact & Gossicop are graph-based datasets curated by Yingtong et al. at https://github.com/safe-graph/GNN-FakeNews/blob/main using the data in FakeNewsNet at https://github.com/KaiDMML/FakeNewsNet

<a href="https://www.politifact.com">Politifact</a>: A website that labels political news articles as real or fake.

<a href="https://www.suggest.com">Gossicop</a> (Renamed to Suggest): A website that labels celebrity news articles as real or fake.

## Research Papers Referenced

<ul>
  <li> Yingtong Dou et al., "User Preference Aware Fake News Detection", July 2021, Retrieved via: https://arxiv.org/abs/2104.12259 </li>
  <li> Yi Han et al., "Graph Neural Networks with Continual Learning for Fake News Detection from Social Media", August 2020, Retrieved via: https://arxiv.org/abs/2007.03316 </li>
  <li> Rex Ying et al., "Hierarchical Graph Prepresentation Learning with Differentiable Pooling", Feb 2019, Retrieved via: https://arxiv.org/abs/1806.08804 </li>
</ul>
