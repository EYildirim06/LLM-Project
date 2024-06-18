# views.py

import io
import base64
import matplotlib.pyplot as plt
from django.shortcuts import render
from .sample1 import SamplingContext, SimpleRandomSampling, IntervalSampling, StratifiedSampling
from .adapters import TSVAdapter
import seaborn as sns

def get_party_distribution(voters):
    party_counts = {'A': 0, 'B': 0, 'C': 0}
    for voter in voters:
        if voter.selection in party_counts:
            party_counts[voter.selection] += 1
    return party_counts

def create_charts(party_distribution):
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    # Bar chart
    sns.barplot(x=list(party_distribution.keys()), y=list(party_distribution.values()), ax=axes[0])
    axes[0].set_title('Party Distribution - Bar Chart')

    # Pie chart
    axes[1].pie(party_distribution.values(), labels=party_distribution.keys(), autopct='%1.1f%%')
    axes[1].set_title('Party Distribution - Pie Chart')

    plt.tight_layout()

    # Save the figure in memory
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    plt.close(fig)
    buffer.seek(0)

    # Encode the image to base64
    image_png = buffer.getvalue()
    buffer.close()
    image_base64 = base64.b64encode(image_png)
    image_base64 = image_base64.decode('utf-8')

    return image_base64

def sample_result(request):
    return render(request, 'sample_result.html')

def sample_simple_random(request):
    strategy = SamplingContext(SimpleRandomSampling())
    simple_sample = strategy.sample_voters()
    simple_tsv = TSVAdapter(simple_sample).get_tsv()

    party_distribution = get_party_distribution(simple_sample)
    chart = create_charts(party_distribution)

    return render(request, 'sample_result.html', {
        'simple_tsv': simple_tsv,
        'chart': chart,
        'chart_title': 'Simple Random Sampling'
    })

def sample_interval(request):
    strategy = SamplingContext(IntervalSampling())
    interval_sample = strategy.sample_voters()
    interval_tsv = TSVAdapter(interval_sample).get_tsv()

    party_distribution = get_party_distribution(interval_sample)
    chart = create_charts(party_distribution)

    return render(request, 'sample_result.html', {
        'interval_tsv': interval_tsv,
        'chart': chart,
        'chart_title': 'Interval Sampling'
    })

def sample_stratified(request):
    strategy = SamplingContext(StratifiedSampling())
    stratified_sample = strategy.sample_voters()
    stratified_tsv = TSVAdapter(stratified_sample).get_tsv()

    party_distribution = get_party_distribution(stratified_sample)
    chart = create_charts(party_distribution)

    return render(request, 'sample_result.html', {
        'stratified_tsv': stratified_tsv,
        'chart': chart,
        'chart_title': 'Stratified Sampling'
    })
